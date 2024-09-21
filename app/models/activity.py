from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), index=True)
    description = Column(Text)
