from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..deps import authenticate_token, get_session
from ..models import Item, ItemBase

router = APIRouter()


@router.post(
    "/users/{user_id}/items/",
    dependencies=[Depends(authenticate_token)],
)
def create_item_for_user(
    user_id: int, item: ItemBase, db: Session = Depends(get_session)
):
    db_item = Item.from_orm(item, update={"user_id": user_id})
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/items/")
def read_items(db: Session = Depends(get_session)):
    items = db.exec(select(Item)).all()
    return items
    