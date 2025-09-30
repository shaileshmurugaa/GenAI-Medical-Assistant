# diagnosis.py
import sqlite3
import time

MAX_PROCESS_SECONDS = 5

# ------------------ Text preprocessing ------------------
def preprocess_text(text):
    text = text.lower()
    tokens = [t.strip() for t in text.replace("/", " ").replace(";", ",").split(",")]
    flat = []
    for t in tokens:
        for w in t.split():
            if w:
                flat.append(w.strip())
    return list(set(flat))

# ------------------ Query DB ------------------
def query_possible_diseases(tokens):
    conn = sqlite3.connect("indian_disease.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, symptoms, treatment FROM disease")
    all_diseases = cursor.fetchall()
    conn.close()

    candidates = []
    for name, symptoms, treatment in all_diseases:
        symptom_tokens = preprocess_text(symptoms)
        overlap = len(set(tokens) & set(symptom_tokens))
        score = overlap / max(len(symptom_tokens), 1)
        if score > 0:
            candidates.append({
                "disease": name,
                "score": score,
                "severity": min(10, int(score * 10)),
                "summary": treatment
            })
    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates

def get_drug_interactions(meds_list):
    return []

# ------------------ Scoring & Response ------------------
def score_candidates(symptom_text, patient_meta):
    start = time.time()
    tokens = preprocess_text(symptom_text)
    candidates = query_possible_diseases(tokens)

    for c in candidates:
        if patient_meta.get("age"):
            age = patient_meta["age"]
            if c["severity"] > 7 and age > 60:
                c["score"] += 0.05
        if c["score"] > 1.0:
            c["score"] = 1.0

    if time.time() - start > MAX_PROCESS_SECONDS:
        raise TimeoutError("Processing exceeded allowed time")

    return candidates[:10]

def build_response(symptom_text, patient_meta, meds_list=None, use_llm=False):
    candidates = score_candidates(symptom_text, patient_meta)

    diffs = []
    for c in candidates:
        diffs.append({
            "disease": c["disease"],
            "confidence": round(c["score"], 2),
            "severity": c["severity"],
            "summary": c["summary"]
        })

    interactions = get_drug_interactions(meds_list) if meds_list else []
    referral = any(c["severity"] >= 8 and c["score"] >= 0.5 for c in candidates)

    llm_note = "LLM refinement not enabled in offline mode." if use_llm else None

    return {
        "differential": diffs,
        "drug_interactions": interactions,
        "referral_recommended": referral,
        "note": llm_note
    }
