from pydantic import BaseModel, Field
from datetime import time, datetime
from time import time
from typing import Optional

class ActivityBase(BaseModel):
    title: str = Field(..., max_length=45, description="The title of the activity")
    description: Optional[str] = Field(None, description="A brief description of the activity") 
    day: int = Field(1, description="Day asigned for the activity") 
    #activity_time: Optional[time] = Field(None, description="The time of  the activity")

class ActivityCreate(ActivityBase):
    pass

class ActivityEdit(ActivityBase):
    id: int = Field(...)

class ActivityResponse(ActivityBase):
    """Returning activity data."""
    id: int = Field(...)
    created_at: datetime = Field(...)

    # Allows compatibility with ORM models
    class Config:
        orm_mode = True 
