from fastapi import APIRouter, HTTPException
from schemas.candidate_schema import CandidateCreate, Candidate
from services import candidate_services
from typing import List

router = APIRouter()


@router.post("/", response_model=Candidate)
def create_candidate(candidate: CandidateCreate):
    try:
        result = candidate_services.create_candidate(candidate)
        return { "id": result[0]["id"], **candidate.dict() }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[Candidate])
def get_candidates():
   try:
       candidates = candidate_services.list_candidates()
       return candidates
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
