from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from financial_record import FinancialRecord
from financial_schema import FinancialCreate
from users import User
from role_check import check_role
from typing import Optional
from datetime import date

router = APIRouter(prefix="/records", tags=["Financial"])

@router.post("/")
def create_record(record: FinancialCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["admin"])

    db_record = FinancialRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return {"message": "Record created successfully", "record_id": db_record.id}

@router.get("/")
def get_records(
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    check_role(current_user, ["admin", "analyst"])

    query = db.query(FinancialRecord).filter(FinancialRecord.is_deleted == False)

    if type:
        query = query.filter(FinancialRecord.type == type)

    if category:
        query = query.filter(FinancialRecord.category == category)

    if start_date:
        query = query.filter(FinancialRecord.date >= start_date)

    if end_date:
        query = query.filter(FinancialRecord.date <= end_date)

    return query.all()

@router.put("/{record_id}")
def update_record(record_id: int, record: FinancialCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["admin"])

    db_record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id, FinancialRecord.is_deleted == False).first()

    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")

    db_record.amount = record.amount
    db_record.type = record.type
    db_record.category = record.category
    db_record.date = record.date
    db_record.description = record.description

    db.commit()
    db.refresh(db_record)

    return {"message": "Record updated successfully"}

@router.delete("/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["admin"])

    db_record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id, FinancialRecord.is_deleted == False).first()

    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")

    db_record.is_deleted = True
    db.commit()

    return {"message": "Record deleted successfully"}