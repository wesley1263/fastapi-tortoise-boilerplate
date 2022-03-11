from app.modules.user.crud import all_user, save_user, find_user_by_id
from app.modules.user.schema import GetUser, CreateAndUpdateUser


async def get_user_list():
    return await all_user()


async def create_a_user(payload: CreateAndUpdateUser) -> GetUser:
    user_id = await save_user(payload)
    return await find_user_by_id(user_id)
