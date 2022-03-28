from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from . import db, models
from .api import items, users


def create_db_and_tables():
    assert models, "Models should be imported so SQLModel has them registered"
    SQLModel.metadata.create_all(db.engine)


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(items.router)


@app.on_event("startup")
def startup_event():
    create_db_and_tables()
