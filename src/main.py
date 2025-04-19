from functools import lru_cache
from fastapi import FastAPI
from yookassa import Configuration
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from core import config

app = FastAPI()
app.include_router(router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@lru_cache
def get_settings():
    return config.Settings()


Configuration.account_id = get_settings().YOO_APP_ID
Configuration.secret_key = get_settings().YOO_SECRET
