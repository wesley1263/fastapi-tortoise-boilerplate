from tortoise.contrib.pydantic import (pydantic_model_creator,
                                       pydantic_queryset_creator,
                                       PydanticListModel)
from tortoise.exceptions import DoesNotExist

from app.modules.user.model import User
from app.modules.user.schema import (CreateAndUpdateUser, GetUser)


async def save_user(payload: CreateAndUpdateUser) -> int:
    user = User(**payload.dict())
    await user.save()
    return user.user_id


async def all_user() -> PydanticListModel:
    users_schemas = pydantic_queryset_creator(User)
    return await users_schemas.from_queryset(User.all())


async def find_user_by_id(user_id: int) -> [GetUser, None]:
    try:
        user_schema = pydantic_model_creator(User)
        user = await User.get_or_none(User.user_id == user_id)
        return user_schema.from_tortoise_orm(user)
    except DoesNotExist:
        return None
