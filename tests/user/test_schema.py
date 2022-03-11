import json

from pydantic import BaseModel

from app.modules.user.schema import CreateAndUpdateUser, GetUser


def test_get_user_schema_should_return_instance_pydantic(user_dict_fake):
    user_schema = GetUser(**user_dict_fake)

    assert isinstance(user_schema, BaseModel)
    assert isinstance(user_schema, GetUser)
    assert isinstance(user_schema.dict(), dict)


def test_get_user_should_return_instance_user_schema(user_dict_fake):
    user_schema = GetUser(**user_dict_fake)

    assert user_schema.user_id == user_dict_fake.get("user_id")
    assert user_schema.name == user_dict_fake.get("name")
    assert user_schema.email == user_dict_fake.get("email")
    assert user_schema.status == user_dict_fake.get("status")


def test_create_user_should_return_instance_user_schema(user_create_dict_fake):
    user_schema = CreateAndUpdateUser(**user_create_dict_fake)

    assert user_schema.name == user_create_dict_fake.get("name")
    assert user_schema.email == user_create_dict_fake.get("email")
    assert user_schema.status == user_create_dict_fake.get("status")
