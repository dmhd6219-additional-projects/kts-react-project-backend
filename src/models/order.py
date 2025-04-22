from typing import List
from pydantic import BaseModel

class OrderRequest(BaseModel):
    user_id: str
    product_ids: List[int]
