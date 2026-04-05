from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from dependencies import get_db, get_current_user
from financial_record import FinancialRecord
from users import User
from role_check import check_role

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary")
def get_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["viewer", "analyst", "admin"])

    income = db.query(func.sum(FinancialRecord.amount)).filter(
        FinancialRecord.type == "income",
        FinancialRecord.is_deleted == False
    ).scalar() or 0

    expense = db.query(func.sum(FinancialRecord.amount)).filter(
        FinancialRecord.type == "expense",
        FinancialRecord.is_deleted == False
    ).scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

@router.get("/category-breakdown")
def category_breakdown(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["viewer", "analyst", "admin"])

    result = db.query(
        FinancialRecord.category,
        func.sum(FinancialRecord.amount)
    ).filter(
        FinancialRecord.type == "expense",
        FinancialRecord.is_deleted == False
    ).group_by(FinancialRecord.category).all()

    return [{"category": r[0], "total": r[1]} for r in result]

@router.get("/recent-activity")
def recent_activity(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["viewer", "analyst", "admin"])

    return db.query(FinancialRecord).filter(
        FinancialRecord.is_deleted == False
    ).order_by(FinancialRecord.id.desc()).limit(5).all()