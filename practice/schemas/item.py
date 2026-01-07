from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

class ItemResp(BaseModel):
  name: str
  description: Optional[str] = None
  price_with_tax: float
