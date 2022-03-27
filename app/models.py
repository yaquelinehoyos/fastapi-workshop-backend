from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    description: Optional[str] = None
    

class User(BaseModel):
    username: str