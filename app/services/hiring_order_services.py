from repositories import hiring_order_repository
from schemas.hiring_order_schema import HiringOrderCreate

def create_hiring_order(data: HiringOrderCreate):
    return hiring_order_repository.insert_hiring_order(data)

def list_hiring_orders():
    return hiring_order_repository.get_all_hiring_orders()
