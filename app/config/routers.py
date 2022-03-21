from fastapi import FastAPI


def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.modules.category import router as category_routers
    from app.modules.core import helthcheck_router
    from app.modules.user import router as user_router

    app.include_router(helthcheck_router.router)
    app.include_router(user_router.router, prefix="/users", tags=["User"])
    app.include_router(category_routers.router, prefix="/categories", tags=["Category"])
