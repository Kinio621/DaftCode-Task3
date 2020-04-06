from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

app.counter = 0

class Patient(BaseModel):
    name: str
    surename: str
class PatientResp(BaseModel):
    id: int
    patient: Patient
@app.post("/patient",response_model=PatientResp)
def root(p: Patient):
    app.counter += 1
    return PatientResp(id=app.counter,patient=p)
