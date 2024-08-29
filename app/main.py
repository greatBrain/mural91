from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from models import Base, engine

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Routers:
# app.include_router(user.router, prefix="/mural")
# app.include_router(admin.router, prefix="/admin")

@app.get("/")
def root():
    return {"Message":"Mural actividades Salmo 91"}


if __name__=="__main__":
   import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=8000)