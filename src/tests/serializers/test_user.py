import json

from app.domain.user import User
from app.serializers.user import UserJsonEncoder


def test_serialize_domain_user():
    user = User(id=1, name="name")

    expected_json = """
        {
            "id": 1,
            "name": "name"
        }
    """

    json_user = json.dumps(user, cls=UserJsonEncoder)

    assert json.loads(json_user) == json.loads(expected_json)
