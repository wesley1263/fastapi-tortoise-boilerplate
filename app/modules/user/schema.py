from pydantic import BaseModel


class GetUser(BaseModel):
    user_id: int
    name: str
    email: str
    status: bool

    class Config:
        orm_mode = True


class CreateAndUpdateUser(BaseModel):
    name: str
    email: str
    status: bool = True
