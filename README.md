# GenAI-Medical-Assistant

genai-medical-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI backend
│   │   ├── diagnosis.py          # Diagnosis logic
│   │   ├── indian_disease.db     # Offline disease database
│   │   └── requirements.txt      # Python dependencies
│   └── venv/                     # Python virtual environment (optional)
│
├── frontend/
│   ├── index.html                # Landing page (GET DIAGNOSED)
│   ├── home.html                 # Chat interface
│   ├── home.css                  # Styles for chat
│   ├── home.js                   # Chat + fetch + voice
│   ├── chat.js                   # Chat logic (multilingual)
│   └── assets/                   # Images, icons (optional)
│
└── README.md                     # Project explanation & instructions
```

---

### ** README.md Template**

```markdown
# GenAI Medical Assistant (Rural Healthcare)

## Overview
**GenAI Medical Assistant** is a multilingual AI-powered medical diagnosis assistant designed for rural healthcare applications. It predicts diseases based on symptoms, evaluates drug interactions, recommends referrals, and provides a user-friendly chat interface.

This system is **offline-capable**, lightweight, and can be deployed even in areas with limited internet access.

---

## Key Innovations

1. **Hybrid AI Model**
   - Combines symbolic logic & knowledge-base reasoning with data-driven heuristics.
   - Fast and explainable predictions without cloud dependency.

2. **BioNERT Integration**
   - Extracts medical entities (symptoms, medications) for better accuracy.
   - Supports drug interaction checks and referral suggestions.

3. **Multilingual Support**
   - Supports 12+ Indian languages (Hindi, Tamil, Telugu, Malayalam, Kannada, Bengali, Gujarati, Marathi, Punjabi, Odia, Urdu, English).
   - Frontend responses dynamically translated offline.

4. **Offline-first Design**
   - Entire diagnosis runs locally using SQLite.
   - Reduces dependency on external APIs, ensuring reliability in rural areas.

5. **User-friendly Chat Interface**
   - ChatGPT-style conversation interface.
   - Optional voice input/output.
   - Language selection allows communication in preferred language.

6. **Smart Referral Recommendations**
   - Flags high-risk conditions based on age, symptom severity, and confidence.

7. **Future-ready IoT/VLSI Integration**
   - Can integrate with vitals-monitoring IoT devices.
   - Potential VLSI-accelerated modules for embedded real-time inference.

---

## Features
- Symptom-based disease prediction
- Multilingual chat interface with voice support
- Drug interaction checks
- Referral recommendation for severe cases
- Offline-first backend
- Easy LAN deployment

---

## Project Structure
```

backend/     → FastAPI + SQLite
frontend/    → HTML, CSS, JS chat interface
README.md    → This file

````

---

## Setup Instructions

### Backend
1. Open terminal in `backend/app`.
2. Create virtual environment:
   ```bash
   python -m venv venv
````

3. Activate environment:

   ```bash
   venv\Scripts\activate    # Windows
   source venv/bin/activate # macOS/Linux
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Start backend server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Frontend

1. Open terminal in `frontend`.
2. Start HTTP server:

   ```bash
   python -m http.server 8080
   ```
3. Open browser at `http://localhost:8080/home.html`

---

## How to Use

1. Select preferred language.
2. Enter symptoms (comma-separated), patient details, and medications.
3. Click **Send** to get diagnosis.
4. Chat assistant responds in selected language with:

   * Differential diagnosis
   * Drug interactions
   * Referral advice

---

## Requirements

* Python 3.10+
* FastAPI
* Uvicorn
* deep-translator
* SQLite3
* Modern browser (Chrome/Firefox/Edge)

---

## Notes

* Designed for rural healthcare and offline use.
* Easily extensible to include IoT sensor data and VLSI modules.

```
---
