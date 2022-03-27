from fastapi import APIRouter

from ..models import User

router = APIRouter()


@router.get("/users/")
def read_users():
    return []


@router.post("/users/")
def create_user(user: User):
    return user


@router.get("/users/{user_id}")
def read_user(user_id: int):
    return {"id": user_id, "username": "Foo"}
