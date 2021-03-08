import json

from app.repository.memrepo import MemRepo
from app.serializers.user import UserJsonEncoder
from app.use_cases.user_list import user_list_use_case
from fastapi import APIRouter

router = APIRouter()

users = [
    {"id": 1, "name": "name1"},
    {"id": 2, "name": "name2"},
    {"id": 3, "name": "name3"},
    {"id": 4, "name": "name4"},
]


@router.get("/users")
def user_list():
    repo = MemRepo(users)
    result = user_list_use_case(repo)

    return json.dumps(result, cls=UserJsonEncoder)
