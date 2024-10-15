from sqlalchemy import Column, Integer, String, Text, DateTime,Time, func
from db.database import Base

class ActivityDataModel(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=45), index=True, nullable=False)
    description = Column(Text, nullable=True)
    day = Column(String, nullable=False, default='Monday')
    created_at = Column(DateTime, server_default = func.now())

    def __repr__(self):
        return "<Activity(id={}, title={}, description={}, day{}, created_at={})>".format(self.id, self.title)
