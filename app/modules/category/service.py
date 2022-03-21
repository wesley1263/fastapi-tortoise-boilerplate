from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.category.crud import CategoryCRUD
from app.modules.category.model import Category
from app.modules.category.schema import (CreateCategory, GetCategory,
                                         UpdateCategory)


class CategoryService:
    async def save_category(self, payload: CreateCategory) -> GetCategory:
        result = await CategoryCRUD().create_category(payload)
        return await self._serializer(result)

    async def update_category(self, payload: UpdateCategory) -> GetCategory:
        await CategoryCRUD().update_category(payload)
        category = await CategoryCRUD().get_category(payload.category_id)
        return await self._serializer(category)

    async def exists_category(self, category_id: int) -> bool:
        result = await CategoryCRUD().get_category(category_id)
        if result:
            return True
        return False

    async def all_category(self):
        categories = await CategoryCRUD().get_all_category()
        return [await self._serializer(category) for category in categories]

    async def _serializer(self, category: Category) -> GetCategory:
        category_schema = pydantic_model_creator(Category)
        result = await category_schema.from_tortoise_orm(category)
        return GetCategory(**result.dict())
