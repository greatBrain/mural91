from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.database import Base, engine, get_db
from models.activity import Activity

Base.metadata.create_all(bind=engine)

app = FastAPI()

db = get_db

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_mural(request: Request, session: Session = Depends(db)):
    #activities = db.query(Activity).all()
    #return templates.TemplateResponse("mural.html", {"request": request, "activities": activities})
    return templates.TemplateResponse("user/mural.html", {"request": request})


if __name__=="__main__":
   import uvicorn
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)