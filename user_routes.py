from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from users import User
from user_schema import UserUpdate
from role_check import check_role

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["admin"])
    return db.query(User).all()

@router.patch("/{user_id}")
def update_user(user_id: int, update_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    check_role(current_user, ["admin"])

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if update_data.role is not None:
        user.role = update_data.role

    if update_data.is_active is not None:
        user.is_active = update_data.is_active

    db.commit()
    db.refresh(user)

    return {"message": "User updated successfully"}