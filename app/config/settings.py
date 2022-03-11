import logging
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
    DEBUG: bool = config("DEBUG", default=False, cast=bool)
    DB_URL = config("DB_URL", default="sqlite://boilerplate.db")
    MODELS: List = [
        "app.modules.core.tortoise",
        "app.modules.user.model",
        "aerich.models",
    ]


def get_settings():
    log.info("Loading Config Application.")
    return Setting()
