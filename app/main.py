from fastapi import FastAPI
from starlette.requests import Request
from routes.activity_routers import router as activity_router
from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# User routers:
app.include_router(activity_router, prefix="/actividades/nueva", tags=["Add new activities"])


# Response for users:
@app.get("/")
def root(request: Request):
    return app.include_router(activity_router, prefix="/mural", tags=["Activities"])

# Response just for admins:
'''@app.get("/mural/panel")
def root_admin(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request":request})'''


if __name__=="__main__":
   import uvicorn
   uvicorn.run(app, host="0.0.0.0", port=8000)