from repositories import candidate_repository
from schemas.candidate_schema import CandidateCreate


def create_candidate(data: CandidateCreate):
    return candidate_repository.insert_candidate(data)


def list_candidates():
    return candidate_repository.get_all_candidates()
# deactivate_candidate


def deactivate_candidate(candidate_id: int):
    return candidate_repository.deactivate_candidate(candidate_id)


def get_candidate_by_id(candidate_id: int):
    return candidate_repository.get_candidate_by_id(candidate_id)


def update_candidate(candidate_id: int, data):
    return candidate_repository.update_candidate(candidate_id, data)
