from typing import List

from app.modules.category.model import Category
from app.modules.category.schema import CreateCategory, UpdateCategory


class CategoryCRUD:

    async def save_category(self, payload: CreateCategory) -> [Category, None]:
        exists = await self.get_category_by_name(payload.name)
        if exists:
            await Category.save(**payload.dict())
            return exists
        return await Category.create(**payload.dict())

    async def create_category(self, payload: CreateCategory) -> Category:
        return await Category.create(**payload.dict())

    async def update_category(self, payload: UpdateCategory):
        return await Category.save(**payload.dict())

    async def get_category(self, category_id: int) -> Category:
        return await Category.get_or_none(category_id=category_id)

    async def get_category_by_name(self, name: str) -> Category:
        return await Category.get_or_none(name=name)

    async def get_all_category(self) -> List[Category]:
        return await Category.all()
