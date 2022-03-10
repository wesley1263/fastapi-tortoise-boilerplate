import logging

from fastapi import FastAPI
from tortoise import Tortoise, run_async
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


async def generate_schema() -> None:
    log.info("Initialize Tortoise...")
    await Tortoise.init(db_url=settings.DB_URL, modules={"models": settings.MODELS})
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
