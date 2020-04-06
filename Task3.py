from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

global i
i=-1

class Patient(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: int
    patient: Patient

@app.post("/patient",response_model=PatientResp)
def root(p: Patient):
    i=i+1
    return PatientResp(id=i,patient=p)
