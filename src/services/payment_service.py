import uuid
from yookassa import Payment

from models.payment import PaymentRequest


def create_payment_yookassa(request: PaymentRequest):
    idempotence_key = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": request.amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "embedded"
        },
        "capture": True,
        "description": request.description
    }, idempotence_key)

    return {"confirmation_token": payment.confirmation.confirmation_token}
