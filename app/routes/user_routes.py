from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId

from app.schemas.user_schema import UserRegister, UserLogin
from app.models.user_model import user_collection
from app.utils.password import hash_password, verify_password
from app.utils.jwt import create_access_token
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

# REGISTER
@router.post("/register", status_code=201)
def register_user(user: UserRegister):
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user_dict = user.dict()
    user_dict["password"] = hash_password(user_dict["password"])

    user_collection.insert_one(user_dict)
    return {"message": "User registered successfully"}

# LOGIN (JWT CREATED HERE)
@router.post("/login")
def login_user(user: UserLogin):
    db_user = user_collection.find_one({"email": user.email})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(str(db_user["_id"]))

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# PROTECTED ROUTE (JWT TEST)
@router.get("/me")
def get_me(user_id: str = Depends(get_current_user)):
    return {
        "message": "JWT working successfully ✅",
        "user_id": user_id
    }

# EXISTING ROUTE
@router.get("/")
def get_all_users():
    return list(user_collection.find({}, {"_id": 0}))
