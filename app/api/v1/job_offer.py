from fastapi import APIRouter, HTTPException
from schemas.job_offer_schema import JobOfferCreate, JobOffer
from services import job_offer_services
from typing import List

router = APIRouter()

@router.post("/", response_model=JobOffer)
def create_job_offer(job_offer: JobOfferCreate):
    try:
        result = job_offer_services.create_job_offer(job_offer)
        return { "id": result[0]["id"], **job_offer.dict() }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[JobOffer])
def get_job_offers():
   try:
       job_offers = job_offer_services.list_job_offers()
       return job_offers
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
