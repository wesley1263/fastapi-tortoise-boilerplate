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
    DYNAMO_ENDPOINT_URL = config("DYNAMO_ENDPOINT_URL")
    DYNAMO_REGION_NAME = config("DYNAMO_REGION_NAME")
    DYNAMO_AWS_ACCESS_KEY_ID = config("DYNAMO_AWS_ACCESS_KEY_ID")
    DYNAMO_AWS_SECRET_ACCESS_KEY = config("DYNAMO_AWS_SECRET_ACCESS_KEY")
    MODELS: List = [
        "app.modules.user.model",
        "app.modules.category.model",
        "aerich.models",
    ]


@lru_cache()
def get_settings():
    log.info("Loading Config Application.")
    return Setting()
