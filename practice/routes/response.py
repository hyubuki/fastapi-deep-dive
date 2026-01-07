from typing import Optional
from fastapi import APIRouter, Form, status
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse

from practice.dto import *

router = APIRouter()

# response_class = JSONResponse (default)
@router.get("/json/{item_id}", response_class=JSONResponse)
async def response_json(item_id: int, q: Optional[str] = None):
  return JSONResponse(
      {"item_id": item_id, "q": q, "message": "hello, JsonParser"},
      status.HTTP_200_OK
  )


@router.get("/html/{item_id}", response_class=HTMLResponse)
async def response_html(item_id: int, item_name: Optional[str] = None):
  html_str = f'''
  <html>
  <body>
    <h2>HTML Response</h2>
    <p>item_id = {item_id}</p>
    <p>item_name = {item_name}</p>
  </body>
  </html>
  '''
  return HTMLResponse(html_str, status.HTTP_200_OK)


@router.get("/redirect")
async def redirect_only(comment: Optional[str] = None):
  print(f"redirect: {comment}")

  return RedirectResponse(url=f"./html/2?item_name={comment}")


# Redirect Post -> Get 으로 전환할 경우
# status_code=status.HTTP_302_FOUND(스펙상 명확하지 않으나 암묵적으로 사용) 또는 status_code=status.HTTP_303_SEE_OTHER 필수
@router.post("/create_redirect")
async def create_item(item_id: int = Form(), item_name: str = Form()):
  print(f"item_id: {item_id}, item_name: {item_name} has been created.")
  return RedirectResponse(
      url=f"./html/{item_id}?item_name={item_name}",
      status_code=status.HTTP_303_SEE_OTHER
  )


# response_model
# @router.post("/create_item", response_model=ItemResp, status_code=status.HTTP_201_CREATED)
@router.post("/create_item", status_code=status.HTTP_201_CREATED)
async def create_item_model(item: Item) -> ItemResp:
  if item.tax:
    price_with_tax = item.price + (item.price * item.tax)
  else:
    price_with_tax = item.price

  resp = ItemResp(name=item.name, description=item.description,
                  price_with_tax=price_with_tax)
  return resp