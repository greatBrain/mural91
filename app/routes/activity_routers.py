from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from db.database import get_db
from models.activity import Activity # Model
from schemas.activity_schema import ActivityResponse, ActivityCreate # Schema

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@router.get("/mural", response_model=List[ActivityResponse])
def get_mural(request:Request, db:Session = Depends(get_db)):
    return templates.TemplateResponse("user/mural.html", {"request":request})



@router.post("/actividades/nueva/", status_code=status.HTTP_201_CREATED, response_model=ActivityResponse)
def add_activity(activity: ActivityCreate, db : Session = Depends(get_db)):

    """Create a new activity."""
    new_activity = Activity(
        title = activity.title,
        description = activity.description,
        created_at =datetime.now() # Set created_at to now or let DB handle it with server_default
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity