from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.database import Base, engine, get_db
from models.activity import ActivityDataModel
from fastapi import HTTPException, status, Depends
from datetime import datetime
from schemas.activity_schema import ActivityCreate, ActivityResponse
from collections import defaultdict

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Root endpoint for user
@app.get("/")
async def get_mural(request: Request, session: Session = Depends(get_db)):
    activities = session.query(ActivityDataModel).all()
    activities_list = []

    # Agrupa los servicios por dias, en un diccionario
    activities_group = defaultdict(list)

    for activity in activities:
        activities_group[activity.day].append({
            "title":activity.title,
            "description":activity.description
            })
    activities_dict = dict(activities_group)

    #return {"activities":activities_dict}
    return templates.TemplateResponse("user/mural.html", {"request": request, "activities":activities_dict})


# endpoint to serve the activities data. A JS will fetch it from client side.
@app.get("/api/getActivities")
async def get_activities():
      pass




# Redirects to a login page:
@app.get("/admin")
async def get_admin_form(request: Request, session: Session = Depends(get_db)):
    return templates.TemplateResponse("admin/login.html", {"request": request})


# USER ADMIN ROUTE HERE #
@app.post("/agregar/", status_code=status.HTTP_201_CREATED, response_model=ActivityResponse)
async def add_activity(activity: ActivityCreate, db : Session = Depends(get_db)):
    """Create a new activity."""
    new_activity = ActivityDataModel(
        title = activity.title,
        description = activity.description,
        day = activity.day,
        created_at = datetime.now()
    )
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity
# End user admin route #

if __name__=="__main__":
   import uvicorn
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)