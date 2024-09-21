from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from db.database import get_db
from models.activity import Activity # Model
from schemas.activity_schema import ActivityResponse # Schema

router = APIRouter()

@router.get("/mural/", response_model=List[ActivityResponse])
def get_week_activities(db:Session = Depends(get_db)):
    pass