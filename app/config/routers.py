from fastapi import FastAPI


def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.modules.core import helthcheck_router

    app.include_router(helthcheck_router.router)
