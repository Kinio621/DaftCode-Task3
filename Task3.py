from fastapi import FastAPI, HTTPException
app = FastAPI()

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: int
    patient: Patient

global i
i = 0

@app.post('/patient', response_model=PatientResp)
def post_patient(p: Patient):
    i=i+1
    return PatientResp(id=i, patient = p)
