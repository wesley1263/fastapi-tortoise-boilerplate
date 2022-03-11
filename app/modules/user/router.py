from typing import List

from fastapi import APIRouter

from app.modules.user.schema import CreateAndUpdateUser, GetUser
from app.modules.user.service import get_user_list, create_a_user

router = APIRouter()


@router.get("/",
            description="Router to list all user registered",
            # response_model=List[GetUser],
            status_code=200)
async def get_all_user():
    return await get_user_list()


@router.post("/",
             description="Router to register a user",
             response_model=GetUser,
             status_code=201)
async def create_user(payload: CreateAndUpdateUser) -> GetUser:
    return await create_a_user(payload)
