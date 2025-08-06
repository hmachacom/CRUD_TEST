from pydantic import BaseModel
from datetime import date
from typing import Optional


class CandidateBase(BaseModel):
    first_name: str
    last_name: str
    document_type: str
    document_number: str
    date_of_birth: date
    rh: Optional[str]
    shipping_city: Optional[str]
    birth_city: Optional[str]
    home_city: Optional[str]


class CandidateCreate(CandidateBase):
    pass


class Candidate(CandidateBase):
    id: int
