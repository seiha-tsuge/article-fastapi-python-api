import json
from unittest import mock

from app.domain.user import User
from fastapi.testclient import TestClient

user_dict = {"id": 1, "name": "name"}

users = [User.from_dict(user_dict)]


@mock.patch("app.rest.user.user_list_use_case")
def test_get(mock_use_case, client: TestClient):
    mock_use_case.return_value = users

    http_response = client.get("/users")

    assert json.loads(http_response.json()) == [user_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
