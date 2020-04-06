from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

app.counter = 0

class PatientRq(BaseModel):
    data: dict
class PatientResp(BaseModel):
    id: int
    patient: dict
@app.post("/patient",response_model=PatientResp)
def root(rq: PatientRq):
    app.counter += 1
    return PatientResp(id=app.counter,patient={"name":rq.data["name"],"surename":rq.data["surename"]})
