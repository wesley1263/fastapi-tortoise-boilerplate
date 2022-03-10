from datetime import datetime

from app.modules.core.tortoise import TextSummary


def test_model_should_return_instance_model_when_invoked():
    params = {
        "url": "http://www.example.com",
        "summary": "Some test",
        "created_at": datetime.now(),
        "teste": 1,
    }
    model = TextSummary(**params)

    assert isinstance(model, TextSummary)
    assert isinstance(model.url, str)
    assert isinstance(model.summary, str)
    assert isinstance(model.created_at, datetime)
