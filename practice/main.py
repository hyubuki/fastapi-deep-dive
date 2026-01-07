from fastapi import FastAPI

from .routes import *

from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.include_router(item.router ,prefix="/item", tags=["item"] )
app.include_router(http_request.router ,prefix="/http_request", tags=["request"] )
app.include_router(response.router, prefix="/response", tags=["response"])

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=1
)
