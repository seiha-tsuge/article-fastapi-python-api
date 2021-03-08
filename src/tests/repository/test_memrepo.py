import pytest
from app.domain.user import User
from app.repository.memrepo import MemRepo


@pytest.fixture
def user_dicts():
    return [
        {"id": 1, "name": "name1"},
        {"id": 2, "name": "name2"},
        {"id": 3, "name": "name3"},
        {"id": 4, "name": "name4"},
    ]


def test_repository_list_without_parameters(user_dicts):
    repo = MemRepo(user_dicts)

    users = [User.from_dict(i) for i in user_dicts]

    assert repo.list() == users
