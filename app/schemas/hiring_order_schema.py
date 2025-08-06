from pydantic import BaseModel
from typing import Optional

class HiringOrderBase(BaseModel):
    client: str
    position: str
    exams: Optional[str] = None

class HiringOrderCreate(HiringOrderBase):
    pass

class HiringOrder(HiringOrderBase):
    id: int
