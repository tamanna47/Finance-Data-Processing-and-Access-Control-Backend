from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from database import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    description = Column(String)
    is_deleted = Column(Boolean, default=False)