from app.domain.user import User


def test_user_model_init():
    user = User(
        id=1,
        name="name",
    )

    assert user.id == 1
    assert user.name == "name"


def test_user_model_from_dict():
    init_dict = {
        "id": 1,
        "name": "name",
    }

    room = User.from_dict(init_dict)

    assert room.id == 1
    assert room.name == "name"


def test_user_model_to_dict():
    init_dict = {
        "id": 1,
        "name": "name",
    }

    room = User.from_dict(init_dict)

    assert room.to_dict() == init_dict


def test_user_model_comparison():
    init_dict = {
        "id": 1,
        "name": "name",
    }

    room1 = User.from_dict(init_dict)
    room2 = User.from_dict(init_dict)

    assert room1 == room2
