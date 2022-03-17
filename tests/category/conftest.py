import pytest
from faker import Factory

faker = Factory.create("pt_BR")


@pytest.fixture
def category_dict_faker():
    return {
        "category_id": faker.random_int(min=1, max=100),
        "name": faker.name(),
        "status": True,
    }
