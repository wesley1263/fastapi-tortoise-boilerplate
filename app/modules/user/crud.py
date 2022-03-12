from typing import List

from app.modules.user.model import User
from app.modules.user.schema import (CreateAndUpdateUser)


async def save_user(payload: CreateAndUpdateUser) -> User:
    return await User.create(**payload.dict())


async def all_user() -> List[User]:
    return await User.all()


async def find_user_by_id(user_id: int) -> [User, None]:
    return await User.get_or_none(user_id=user_id)
