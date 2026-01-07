from fastapi import FastAPI, Request, Body
from typing import Optional, Annotated

from practice.request import Item

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(request: Request, item_id: int, receipt: str) :
  client_host = request.client.host
  headers = request.headers
  url = request.url
  http_method = request.method
  path_params = request.path_params
  query_params = request.query_params

  return {
    "item_id": item_id,
    "client_host": client_host,
    "headers": headers,
    "path_params": path_params,
    "query_params": query_params,
    "url": url,
    "http_method": http_method
    # "item": item
  }