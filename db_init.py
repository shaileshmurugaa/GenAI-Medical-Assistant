# db_init.py
import sqlite3
from pathlib import Path
from config import BASE_DIR
DB_PATH = Path(BASE_DIR) / "medical_kb.db"

def create_and_seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # diseases table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease_name TEXT,
        symptoms TEXT,
        severity_score INTEGER,
        summary TEXT
    )
    """)
    # drug interactions
    cur.execute("""
    CREATE TABLE IF NOT EXISTS drug_interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drug_a TEXT,
        drug_b TEXT,
        note TEXT
    )
    """)
    # seed small synthetic entries (expand later)
    cur.execute("DELETE FROM diseases")
    sample = [
        ("Dengue", "fever,headache,muscle pain,rash,nausea", 7, "Viral infection transmitted by mosquitoes; look for high fever and thrombocytopenia."),
        ("Malaria", "fever,chills,headache,sweating,muscle pain", 8, "Parasitic infection; rapid tests and blood smear needed; consider urgent referral if severe."),
        ("Urinary Tract Infection", "dysuria,frequency,lower abdominal pain,fever", 5, "Common bacterial infection; antibiotics based on local protocols."),
        ("Pulmonary TB", "chronic cough,weight loss,fever,night sweats", 9, "Consider sputum testing and referral to TB program."),
        ("Acute Gastroenteritis", "diarrhea,vomiting,abdominal pain,fever", 6, "Hydration and rehydration therapy; evaluate for dehydration.")
    ]
    for d in sample:
        cur.execute("INSERT INTO diseases (disease_name, symptoms, severity_score, summary) VALUES (?,?,?,?)", d)
    # sample drug interactions
    cur.execute("DELETE FROM drug_interactions")
    interactions = [
        ("aspirin", "warfarin", "Increased bleeding risk - avoid combination without monitoring."),
        ("ciprofloxacin", "tizanidine", "Severe hypotension risk - contraindicated."),
    ]
    for a,b,n in interactions:
        cur.execute("INSERT INTO drug_interactions (drug_a,drug_b,note) VALUES (?,?,?)", (a,b,n))
    conn.commit()
    conn.close()
    print("DB initialized at", DB_PATH)

if __name__ == "__main__":
    create_and_seed()
