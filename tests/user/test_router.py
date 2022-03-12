import pytest


def test_users_should_return_ok_when_invoked(test_app):
    response = test_app.get("/users/")

    assert response.status_code == 200


def test_user_post_should_return_201_when_payload_valid(test_app_with_db, user_create_dict_fake):
    response = test_app_with_db.post("/users/", json=user_create_dict_fake)
    user_create_dict_fake["user_id"] = response.json()["user_id"]

    assert response.status_code == 201
    assert response.json() == user_create_dict_fake


def test_user_post_should_return_422_when_payload_invalid(test_app_with_db):
    response = test_app_with_db.post("/users/", json={"email": "test@example.com", "status": False})

    assert response.status_code == 422


def test_user_get_with_param_should_return_200_when_param_is_valid(test_app_with_db):
    response = test_app_with_db.post("/users/", json={"email": "test@example.com", "status": False})

    assert response.status_code == 422


@pytest.fixture(scope="session")
def user_created(test_app_with_db, user_create_dict_fake):
    response = test_app_with_db.post("/users/", json=user_create_dict_fake)
    return response.json()


def test_user_get_should_return_200_when_id_exist(test_app_with_db, user_created):
    id_user = user_created.get("user_id")
    response = test_app_with_db.get(f"/users/{id_user}")

    assert response.status_code == 200
    for key, value in user_created.items():
        assert user_created[key] == value


def test_user_get_should_return_200_when_id_exist(test_app_with_db):
    user_id = 10001
    response = test_app_with_db.get(f"/users/{user_id}")

    assert response.status_code == 404
