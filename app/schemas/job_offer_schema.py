from pydantic import BaseModel
from typing import Optional

class JobOfferBase(BaseModel):
    client: str
    position: str
    city: str
    description: Optional[str] = None

class JobOfferCreate(JobOfferBase):
    pass

class JobOffer(JobOfferBase):
    id: int
