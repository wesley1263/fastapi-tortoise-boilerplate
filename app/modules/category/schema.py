from typing import Optional

from pydantic import BaseModel


class CategorySchema(BaseModel):
    name: str
    status: bool = True


class GetCategory(BaseModel):
    category_id: int
    name: str
    status: bool = True


class CreateAndUpdateCategory(BaseModel):
    name: str
    status: Optional[bool] = True
