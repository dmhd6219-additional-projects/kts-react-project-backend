from pydantic import BaseModel


class PaymentRequest(BaseModel):
    amount: str
    description: str


