from app.domain.user import User


def test_user_model_init():
    user = User(
        id=1,
        name="name",
    )

    assert user.id == 1
    assert user.name == "name"


def test_user_model_from_dict():
    init_dict = {"id": 1, "name": "name"}

    user = User.from_dict(init_dict)

    assert user.id == 1
    assert user.name == "name"


def test_user_model_to_dict():
    init_dict = {"id": 1, "name": "name"}

    user = User.from_dict(init_dict)
    assert user.to_dict() == init_dict


def test_user_model_comparison():
    init_dict = {"id": 1, "name": "name"}

    user1 = User.from_dict(init_dict)
    user2 = User.from_dict(init_dict)

    assert user1 == user2
