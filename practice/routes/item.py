from fastapi import APIRouter, Request, Body
from ..dto import *

router = APIRouter()

@router.post("/items")
async def read_items(item: Item):
  return {"item": item, "message": "api success"}

