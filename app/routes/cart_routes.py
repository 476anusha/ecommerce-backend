from fastapi import APIRouter
from app.schemas.cart_schema import CartItem
from app.models.cart_model import cart_collection

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/add")
def add_to_cart(item: CartItem):
    cart_collection.insert_one(item.dict())
    return {"message": "Item added to cart"}

@router.get("/{user_id}")
def view_cart(user_id: str):
    return list(cart_collection.find({"user_id": user_id}, {"_id": 0}))

@router.delete("/remove/{user_id}/{product_id}")
def remove_item(user_id: str, product_id: str):
    cart_collection.delete_one({"user_id": user_id, "product_id": product_id})
    return {"message": "Item removed"}

@router.delete("/clear/{user_id}")
def clear_cart(user_id: str):
    cart_collection.delete_many({"user_id": user_id})
    return {"message": "Cart cleared"}
