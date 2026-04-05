from pydantic import BaseModel
from datetime import date

class FinancialCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    description: str

class FinancialResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    description: str

    class Config:
        from_attributes = True