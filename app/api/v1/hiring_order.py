from fastapi import APIRouter, HTTPException
from schemas.hiring_order_schema import HiringOrderCreate, HiringOrder
from services import hiring_order_services
from typing import List

router = APIRouter()

@router.post("/", response_model=HiringOrder)
def create_hiring_order(hiring_order: HiringOrderCreate):
    try:
        result = hiring_order_services.create_hiring_order(hiring_order)
        return { "id": result[0]["id"], **hiring_order.dict() }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[HiringOrder])
def get_hiring_orders():
   try:
       hiring_orders = hiring_order_services.list_hiring_orders()
       return hiring_orders
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
