from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserData(BaseModel):
    name: str
    id_number: str
    phone_number: str

@app.post("/risk-score")
def calculate_risk(data: UserData):
    score = 82
    flags = []

    if data.phone_number.startswith("09"):
        flags.append("Mobile number format valid")
    if data.id_number.startswith("A"):
        flags.append("Taiwan ID detected")
    else:
        flags.append("Suspicious ID format")

    level = "High" if score > 70 else "Low"

    return {
        "risk_score": score,
        "risk_level": level,
        "flags": flags
    }