from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.user.crud import (all_user, save_user, find_user_by_id)
from app.modules.user.model import User
from app.modules.user.schema import GetUser, CreateAndUpdateUser


async def get_user_list():
    return [await _serializer(user) for user in await all_user()]


async def create_a_user(payload: CreateAndUpdateUser) -> GetUser:
    user = await save_user(payload)
    return await _serializer(user)


async def find_a_user_by_id(user_id: int) -> [GetUser, None]:
    user = await find_user_by_id(user_id)
    if not user:
        return None
    return await _serializer(user)


async def _serializer(user: User) -> GetUser:
    user_schema = pydantic_model_creator(User)
    result = await user_schema.from_tortoise_orm(user)
    return GetUser(**result.dict())
