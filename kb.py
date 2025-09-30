# kb.py
import sqlite3
from pathlib import Path
from config import BASE_DIR
DB_PATH = Path(BASE_DIR) / "medical_kb.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def query_possible_diseases(symptom_tokens):
    """
    Simple retrieval: match symptoms to disease symptom table and score by overlap.
    symptom_tokens: list of strings
    Returns list of (disease, score, details)
    """
    conn = get_conn()
    cur = conn.cursor()
    # naive: select all diseases and compute overlap
    cur.execute("SELECT id, disease_name, symptoms, severity_score, summary FROM diseases")
    results = []
    for row in cur.fetchall():
        kb_symptoms = [s.strip().lower() for s in row["symptoms"].split(",") if s.strip()]
        overlap = len(set(kb_symptoms) & set(symptom_tokens))
        score = overlap / max(1, len(kb_symptoms))
        if overlap > 0:
            results.append({
                "disease": row["disease_name"],
                "score": float(score),
                "severity": row["severity_score"],
                "summary": row["summary"]
            })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def get_drug_interactions(drug_list):
    conn = get_conn()
    cur = conn.cursor()
    interactions = []
    for i, d in enumerate(drug_list):
        for j, d2 in enumerate(drug_list):
            if i >= j: continue
            cur.execute("SELECT note FROM drug_interactions WHERE (drug_a=? AND drug_b=?) OR (drug_a=? AND drug_b=?)", (d.lower(), d2.lower(), d2.lower(), d.lower()))
            row = cur.fetchone()
            if row:
                interactions.append(row["note"])
    return interactions
