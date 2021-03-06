import json

from app.domain.user import User
from app.serializers.user import UserJsonEncoder


def test_serialize_domain_room():

    user = User(
        id=1,
        name="name",
    )

    expected_json = """
        {
            "id": 1,
            "name": "name"
        }
    """

    json_room = json.dumps(user, cls=UserJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
