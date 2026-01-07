from typing import Optional
from pydantic import BaseModel

class ItemResp(BaseModel):
  name: str
  description: Optional[str] = None
  price_with_tax: float