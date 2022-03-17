from typing import List

from app.modules.category.crud import CategoryCRUD
from app.modules.category.model import Category
from app.modules.category.schema import CreateAndUpdateCategory, GetCategory, CategorySchema
from tortoise.contrib.pydantic import pydantic_model_creator


class CategoryService:

    async def save_category(self, payload: CreateAndUpdateCategory) -> GetCategory:
        category = await CategoryCRUD().save_category(payload)
        return await self._serializer(category)

    async def _serializer(self, category: Category) -> GetCategory:
        category_schema = pydantic_model_creator(Category)
        result = await category_schema.from_tortoise_orm(category)
        return GetCategory(**result.dict())

    async def all_category(self):
        categories = await CategoryCRUD().get_all_category()
        return [await self._serializer(category) for category in categories]
