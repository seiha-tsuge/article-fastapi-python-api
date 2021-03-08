from unittest import mock

import pytest
from app.domain.user import User
from app.use_cases.user_list import user_list_use_case


@pytest.fixture
def domain_users():
    user_1 = User(id=1, name="name1")
    user_2 = User(id=2, name="name2")
    user_3 = User(id=3, name="name3")
    user_4 = User(id=4, name="name4")

    return [user_1, user_2, user_3, user_4]


def test_user_list_without_parameters(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    result = user_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_users
