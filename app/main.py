from fastapi import FastAPI
from app.routes import user_routes, product_routes, cart_routes, order_routes

app = FastAPI(title="E-Commerce Backend API")

app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(cart_routes.router)
app.include_router(order_routes.router)

@app.get("/")
def home():
    return {"status": "E-Commerce API is running"}
