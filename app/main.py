from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.activity_routers import router as activity_router
from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# User routers:
app.include_router(activity_router, prefix="/mural", tags=["Activities"])
app.include_router(activity_router, prefix="/actividades/nueva", tags=["Add new activities"])

# Admin routers:

@app.get("/")
def root():
    return {"Message":"Mural actividades Salmo 91"}

if __name__=="__main__":
   import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=8000)