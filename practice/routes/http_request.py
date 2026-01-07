from fastapi import APIRouter, Request

router = APIRouter()

@router.get("")
async def read_item(request: Request) :
  client_host = request.client.host
  headers = request.headers
  url = request.url
  http_method = request.method
  path_params = request.path_params
  query_params = request.query_params

  return {
    "http_method": http_method,
    "client_host": client_host,
    "url": url,
    "headers": headers,
    "path_params": path_params,
    "query_params": query_params
  }