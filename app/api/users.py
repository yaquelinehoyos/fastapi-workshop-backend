from fastapi import APIRouter, Depends

from ..deps import authenticate_token
from ..models import User

router = APIRouter()


@router.get("/users/")
def read_users():
    return []


@router.post("/users/", dependencies = [Depends(authenticate_token)])
def create_user(user: User):
    return user


@router.get("/users/{user_id}")
def read_user(user_id: int):
    return {"id": user_id, "username": "Foo"}
