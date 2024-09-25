from fastapi import APIRouter, HTTPException, status, Depends
from models.activity import ActivityDataModel
from sqlalchemy.orm import Session
from datetime import datetime
from db.database import get_db
from schemas.activity_schema import ActivityCreate, ActivityResponse

router = APIRouter()

@router.post("/agregar/", status_code=status.HTTP_201_CREATED, response_model=ActivityResponse)
async def add_activity(activity: ActivityCreate, db : Session = Depends(get_db)):

    """Create a new activity."""
    new_activity = ActivityDataModel(
        title = activity.title,
        description = activity.description,
        created_at = datetime.now()
    )
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity