import pytest
from starlette.testclient import TestClient

from app.config.settings import Setting, get_settings
from app.main import create_app


def get_settings_overide():
    return Setting(TESTING=True, DB_URL="sqlite://test_boilerplate.db")


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_overide()
    with TestClient(app) as test_client:
        yield test_client
