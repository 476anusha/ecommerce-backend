from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate
from app.models.product_model import product_collection

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/add")
def add_product(product: ProductCreate):
    product_collection.insert_one(product.dict())
    return {"message": "Product added"}

@router.get("/")
def list_products():
    return list(product_collection.find({}, {"_id": 0}))

@router.get("/{name}")
def get_product(name: str):
    product = product_collection.find_one({"name": name}, {"_id": 0})
    return product

@router.delete("/{name}")
def delete_product(name: str):
    product_collection.delete_one({"name": name})
    return {"message": "Product deleted"}
