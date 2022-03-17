import logging

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.starlette import register_tortoise

from .settings import get_settings

settings = get_settings()

log = logging.getLogger("uvicorn")

TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI):
    """This function is to configuration database credentials"""
    register_tortoise(
        app=app,
        db_url=settings.DB_URL,
        generate_schemas=False,
        modules={"models": settings.MODELS},
    )


async def connect_to_database() -> None:
    log.info("Initialize Tortoise...")
    await Tortoise.init(db_url=settings.DB_URL, modules={"models": settings.MODELS})


async def close_connection_database() -> None:
    log.info("Closing Tortoise...")
    await Tortoise.close_connections()
