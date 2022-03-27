from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import items, users

app = FastAPI()

origins = [
    "http://localhost:8080",
    "https://fastapiworkshop.yaquelinehoyos.com"
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
