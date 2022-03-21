import logging
from functools import lru_cache
from typing import List

from decouple import config
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Setting(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="0.0.1")
    APP_NAME: str = config("APP_NAME", default="FastApi Boilerplate")
    APP_PORT: int = config("APP_PORT", default=8000, cast=int)
    ENVIRONMENT: str = config("ENVIRONMENT", default="dev")
    TESTING: bool = config("TESTING", default=False, cast=bool)
    DB_URL = config("DB_URL")
    DB_TEST_URL = config("DB_TEST_URL")
    ALLOW_HEADERS: List = ["*"]
    ALLOW_METHODS: List = ["*"]
    ORIGINS: List = [
        "http://localhost",
        "http://localhost:8080",
    ]
    MODELS: List = [
        "app.modules.user.model",
        "app.modules.category.model",
        "aerich.models",
    ]


@lru_cache()
def get_settings():
    log.info("Loading Config Application.")
    return Setting()
