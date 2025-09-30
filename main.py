# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from diagnosis import build_response

# FastAPI app
app = FastAPI(title="GenAI Medical Diagnosis Assistant", version="0.1.0")

# Enable CORS for LAN/phone testing
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://192.168.165.231",  # your PC LAN IP
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- Models -------------------
class PatientInfo(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    location: Optional[str] = None

class DiagnoseRequest(BaseModel):
    symptoms: str
    history: Optional[str] = None
    vitals: Optional[str] = None
    meds: Optional[List[str]] = []
    patient: Optional[PatientInfo] = None

# ------------------- Routes -------------------
@app.post("/diagnose")
def diagnose(req: DiagnoseRequest):
    patient_meta = {
        "name": req.patient.name if req.patient else None,
        "age": req.patient.age if req.patient else None,
        "gender": req.patient.gender if req.patient else None
    }
    result = build_response(req.symptoms, patient_meta, meds_list=req.meds)
    return result
