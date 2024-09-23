
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = "sqlite:///./mural.db"

# Connection engine:
engine = create_engine(DATABASE, connect_args={"check_same_thread": False})
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get a session of database in each request
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
    
