from tortoise.models import Model

from app.modules.category.model import Category


def test_model_return_instance_category_when_inkoked(category_dict_faker):
    model = Category(**category_dict_faker)

    assert isinstance(model, Category)
    assert isinstance(model, Model)
