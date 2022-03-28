from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..deps import authenticate_token, get_session
from ..models import User, UserBase

router = APIRouter()


@router.post(
    "/users/",
    dependencies=[Depends(authenticate_token)],
)
def create_user(user: UserBase, db: Session = Depends(get_session)):
    db_user = User.from_orm(user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/")
def read_users(db: Session = Depends(get_session)):
    users = db.exec(select(User)).all()
    return users


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = db.exec(select(User).where(User.id == user_id)).first()
    return db_user
