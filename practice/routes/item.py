from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse


from ..schemas import *

router = APIRouter()

templates = Jinja2Templates(directory="practice/template")

@router.post("/items")
async def read_items(item: Item):
  return {"item": item, "message": "api success"}


@router.get("/item_gubun")
async def read_item_gubun(request: Request, gubun: str):
  item = Item(name="test_item", description="test description", price=1000, tax=0.1)
  return templates.TemplateResponse(
      request=request,
      name="item_gubun.html",
      context={"gubun": gubun, "item": item}
  )

@router.get("/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: int, q: Optional[str] = None ):
  item = Item(name="test_item", description="test description", price=1000, tax=0.1)
  item_dict = item.model_dump()

  return templates.TemplateResponse(
      request=request,
      name="item.html",
      context={"id": id, "q": q, "item": item, "item_dict": item_dict}
  )