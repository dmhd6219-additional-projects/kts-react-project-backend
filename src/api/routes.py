from typing import List

from fastapi import APIRouter, HTTPException

from models.payment import PaymentRequest
from models.user import UserLoginRequest, UserLoginResponse
from models.order import OrderRequest

from services.payment_service import create_payment_yookassa
from services.auth_service import authenticate_user, create_user, save_order, get_orders

router = APIRouter()


@router.post("/login", response_model=UserLoginResponse)
def login(user: UserLoginRequest):
    if authenticate_user(user.username, user.password):
        return {"message": "Login successful", "user_id": user.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post("/register", status_code=201, response_model=UserLoginResponse)
def register(user: UserLoginRequest):
    if not authenticate_user(user.username, user.password):
        created_user = create_user(user.username, user.password)
        return {"message": "Login successful", "user_id": created_user}
    raise HTTPException(status_code=409, detail="User already exists")


@router.get("/orders", response_model=List[int])
def orders(user_id: str):
    return get_orders(user_id)


@router.post("/create-payment")
def create_payment(request: PaymentRequest):
    try:
        return create_payment_yookassa(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-order")
def create_order(request: OrderRequest):
    save_order(request.user_id, request.product_ids)
