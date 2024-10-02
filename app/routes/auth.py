from fastapi import APIRouter, HTTPException, Depends
from app.models import User, Login
from app.core.security import get_password_hash