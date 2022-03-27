from fastapi import APIRouter

from ..models import Item

router = APIRouter()


@router.post("/users/{user_id}/items/")
def create_item_for_use(user_id: int, item: Item):
    return item


@router.get("/items/")
def read_items():
    return []