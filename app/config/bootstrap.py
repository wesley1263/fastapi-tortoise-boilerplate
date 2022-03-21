import logging

from fastapi import FastAPI

from app.config.db import (close_connection_database, connect_to_database,
                           init_db)
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers
from app.config.settings import get_settings

setting = get_settings()
log = logging.getLogger("uvicorn")


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(title=setting.APP_NAME, version=setting.APP_VERSION)
    init_routers(application)
    init_db(application)
    init_middlewares(application)
    return application


app = create_app()


@app.on_event("startup")
async def statup_event():
    log.info("Starting up...")
    await connect_to_database()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
    close_connection_database()
