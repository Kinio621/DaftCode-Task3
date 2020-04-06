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

def increment():
    global i
    i = i + 1
    
@app.post('/patient', response_model=PatientResp)
def post_patient(p: Patient):
    global i
    increment()
    return PatientResp(id=i, patient = p)
