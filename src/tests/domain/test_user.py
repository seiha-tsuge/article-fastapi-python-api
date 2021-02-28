from app.domain.user import User


def test_user_model_init():
    user = User(
        id=1,
        name="name",
    )

    assert user.id == 1
    assert user.name == "name"
