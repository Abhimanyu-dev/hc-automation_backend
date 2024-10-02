from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Appointment(BaseModel):
    patient_id: str
    doctor_id: str
    date: datetime
    notes: Optional[str]

class Referral(BaseModel):
    appointment_id: str
    referred_to: str
    status: str