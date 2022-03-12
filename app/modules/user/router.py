from typing import List

from fastapi import APIRouter, HTTPException

from app.modules.user.schema import CreateAndUpdateUser, GetUser
from app.modules.user.service import (create_a_user, find_a_user_by_id,
                                      get_user_list, remove_a_user)

router = APIRouter()


@router.get(
    "/",
    description="Router to list all user registered",
    response_model=List[GetUser],
    status_code=200,
)
async def get_all_user():
    return await get_user_list()


@router.get(
    "/{user_id}",
    description="Router to list all user registered",
    response_model=GetUser,
    status_code=200,
)
async def get_all_user(user_id: int):
    user = await find_a_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post(
    "/",
    description="Router to register a user",
    response_model=GetUser,
    status_code=201,
)
async def create_user(payload: CreateAndUpdateUser):
    return await create_a_user(payload)


@router.delete("/{user_id}", description="Router to remove a user", status_code=204)
async def create_user(user_id: int):
    result = await remove_a_user(user_id)
    if not result:
        raise HTTPException(status_code=400, detail="User ID not found")
    return {"msg": "User has been removed"}
