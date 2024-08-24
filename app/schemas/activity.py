from pydantic import BaseModel
import datetime

class ActivityBase(BaseModel):
        title:str
        description:str
        time:datetime.time

class ActivityEdit(ActivityBase):
        pass
