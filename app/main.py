from fastapi import FastAPI
from app.routes import auth, appointment

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags={"Authentication"})
app.include_router(appointment.router, prefix="/appointments", tags={"Appointments"})

@app.get("/")
async def root():
    return {"message": "Welcome"}