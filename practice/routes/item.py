from fastapi import APIRouter, Request

item_router = APIRouter()

@item_router.get("")
async def read_items():
  return {"Hello": "World"}