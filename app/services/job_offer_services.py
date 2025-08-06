from repositories import job_offer_repository
from schemas.job_offer_schema import JobOfferCreate

def create_job_offer(data: JobOfferCreate):
    return job_offer_repository.insert_job_offer(data)

def list_job_offers():
    return job_offer_repository.get_all_job_offers()
