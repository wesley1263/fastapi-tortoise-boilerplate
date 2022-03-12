import pytest
from faker import Factory

from app.modules.user.model import User
from app.modules.user import schema

faker = Factory.create("pt_BR")


@pytest.fixture
def user_create_dict_fake():
    return {"name": faker.name(), "email": faker.email(), "status": True}


@pytest.fixture
def user_dict_fake():
    return {
        "user_id": faker.random_int(min=1, max=100),
        "name": faker.name(),
        "email": faker.email(),
        "status": True,
    }


@pytest.fixture
def user_create_dict_fake():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "status": True,
    }


@pytest.fixture
def user_model_fake(user_dict_fake):
    return User(**user_dict_fake)


@pytest.fixture
def user_schema_create_fake(user_dict_fake):
    return schema.CreateAndUpdateUser(**user_dict_fake)
