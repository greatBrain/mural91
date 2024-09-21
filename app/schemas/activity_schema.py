from pydantic import BaseModel, Field
from datetime import time, datetime
from typing import Optional

class ActivityBase(BaseModel):
    title: str = Field(..., max_length=45, description="The title of the activity")
    description: Optional[str] = Field(None, description="A brief description of the activity")
    activity_time: time = Field(..., description="The time associated with the activity")

class ActivityCreate(ActivityBase):    
    pass

class ActivityEdit(ActivityBase):    
    id: int = Field(...)

class ActivityResponse(ActivityBase):
    """Returning activity data."""
    id: int = Field(...)
    created_at: datetime = Field(...)

    class Config:
        orm_mode = True  # Allows compatibility with ORM models
