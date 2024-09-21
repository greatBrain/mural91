from sqlalchemy import Column, Integer, String, Text, DateTime, func
from db.database import Base

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=45), index=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default = func.now(), nulleable = False)

    def __repr__(self):
        return "<Activity(id={}, title={}, description={}, created_at={})>".format(self.id, self.title, 
                                                                                   self.description, self.created_at)
    

''' NOTE: the server_default = func.now() ensures that current timestamp 
is set by the database when a new record is created.'''