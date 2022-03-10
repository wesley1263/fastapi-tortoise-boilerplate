import logging

from fastapi import FastAPI

from app.config.db import init_db
from app.config.routers import init_routers
from app.config.settings import get_settings

setting = get_settings()
log = logging.getLogger("uvicorn")


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(title=setting.APP_NAME, version=setting.APP_VERSION)
    init_routers(application)
    return application


app = create_app()


@app.on_event("startup")
async def statup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
