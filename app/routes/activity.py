from fastapi import APIRouter
from typing import Annotated

router = APIRouter()

@router.get("/mural/")
async def get_activities():
    pass