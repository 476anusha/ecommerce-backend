from fastapi import APIRouter
from app.schemas.order_schema import OrderCreate
from app.models.order_model import order_collection

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/place")
def place_order(order: OrderCreate):
    order_collection.insert_one(order.dict())
    return {"message": "Order placed successfully"}

@router.get("/{user_id}")
def get_user_orders(user_id: str):
    return list(order_collection.find({"user_id": user_id}, {"_id": 0}))
