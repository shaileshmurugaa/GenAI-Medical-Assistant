import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("indian_disease.db")
cursor = conn.cursor()

# Step 1: Create the disease table
cursor.execute("""
CREATE TABLE IF NOT EXISTS disease (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    symptoms TEXT,
    treatment TEXT
)
""")

# Step 2: Populate with common Indian diseases (synthetic sample data)
diseases = [
    ("Dengue", "fever, headache, joint pain, rash", "hydration, paracetamol, rest"),
    ("Malaria", "fever, chills, sweating, headache", "antimalarial drugs, hydration"),
    ("Typhoid", "fever, abdominal pain, weakness, diarrhea", "antibiotics, hydration"),
    ("Chikungunya", "fever, joint pain, rash, headache", "hydration, pain relievers, rest"),
    ("Common Cold", "sneezing, cough, runny nose, sore throat", "rest, fluids, paracetamol"),
    ("COVID-19", "fever, cough, breathlessness, fatigue", "isolation, supportive care, antivirals if prescribed"),
    ("Tuberculosis", "persistent cough, fever, night sweats, weight loss", "antitubercular therapy (ATT)"),
    ("Jaundice", "yellowing of eyes, fatigue, nausea, dark urine", "hydration, rest, monitoring liver function"),
    ("Hypertension", "headache, dizziness, nosebleeds", "lifestyle changes, antihypertensive drugs"),
    ("Diabetes", "frequent urination, excessive thirst, fatigue", "diet control, insulin/oral medications")
]

# Insert data into the table
cursor.executemany("INSERT INTO disease (name, symptoms, treatment) VALUES (?, ?, ?)", diseases)

conn.commit()
conn.close()
print("Indian disease database created successfully!")
