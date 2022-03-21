def test_post_category_should_return_201_when_payload_valid(
    category_dict_faker, test_app_with_db
):
    response = test_app_with_db.post("/categories/", json=category_dict_faker)

    payload = response.json()
    assert response.status_code == 201
    for key, value in payload.items():
        assert payload[key] == value


def test_post_category_should_return_422_when_payload_invalid(test_app_with_db):
    response = test_app_with_db.post(
        "/categories/", json={"status": True, "category_id": 1}
    )

    assert response.status_code == 422


def test_list_category_should_return_200_list_when_requested(test_app_with_db):
    response = test_app_with_db.get("/categories/")

    assert response.status_code == 200
