from typing import List

from fastapi import APIRouter
from starlette import status

from app.modules.category.schema import (CategorySchema, CreateCategory,
                                         GetCategory)
from app.modules.category.service import CategoryService

router = APIRouter()


@router.post(
    "/",
    description="This router is to register new category",
    response_model=GetCategory,
    status_code=status.HTTP_201_CREATED,
)
async def post_category(payload: CreateCategory):
    return await CategoryService().save_category(payload)


@router.get(
    "/",
    description="This router receive a list category",
    response_model=List[CategorySchema],
    status_code=status.HTTP_200_OK,
)
async def list_category():
    return await CategoryService().all_category()
