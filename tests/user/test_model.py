from tortoise.models import Model

from app.modules.user.model import User


def test_model_should_return_instance_tortoise_when_inkoked(user_model_fake):
    assert isinstance(user_model_fake, Model)


def test_model_should_return_instance_user_when_inkoked(user_model_fake):
    assert isinstance(user_model_fake, User)
    assert isinstance(user_model_fake.user_id, int)
    assert isinstance(user_model_fake.name, str)
    assert isinstance(user_model_fake.email, str)
    assert isinstance(user_model_fake.status, bool)


def test_model_should_return_str_name_when_name_defined(user_model_fake):
    assert user_model_fake.__str__() == user_model_fake.name
