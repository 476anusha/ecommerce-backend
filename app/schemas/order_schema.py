from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: str
    order_id: str
    total_amount: float
