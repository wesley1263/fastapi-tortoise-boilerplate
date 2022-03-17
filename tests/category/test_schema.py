from pydantic import BaseModel

from app.modules.category.schema import CreateAndUpdateCategory, GetCategory, CategorySchema


def test_get_category_schema_should_return_instance_when_invoked(category_dict_faker):
    schema = GetCategory(**category_dict_faker)

    assert isinstance(schema, GetCategory)
    assert isinstance(schema, BaseModel)
    assert isinstance(schema.category_id, int)
    assert isinstance(schema.name, str)
    assert isinstance(schema.status, bool)


def test_category_schema_create_and_update_should_return_instance_when_invoked(
        category_dict_faker,
):
    schema = CreateAndUpdateCategory(**category_dict_faker)

    assert isinstance(schema, CreateAndUpdateCategory)
    assert isinstance(schema, BaseModel)
    assert isinstance(schema.name, str)
    assert isinstance(schema.status, bool)


def test_category_schema_should_return_instance_when_invoked(
        category_dict_faker,
):
    schema = CategorySchema(**category_dict_faker)

    assert isinstance(schema, CategorySchema)
    assert isinstance(schema, BaseModel)
    assert isinstance(schema.name, str)
    assert isinstance(schema.status, bool)
