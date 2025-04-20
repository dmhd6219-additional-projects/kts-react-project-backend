from fastapi import APIRouter, HTTPException

from models.payment import PaymentRequest
from services.payment_service import create_payment_yookassa
from core.config import get_settings

router = APIRouter()


@router.post("/create-payment")
def create_payment(request: PaymentRequest):
    try:
        return create_payment_yookassa(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))