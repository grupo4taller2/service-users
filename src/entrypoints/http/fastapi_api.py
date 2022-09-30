from fastapi import APIRouter
from typing import Any

from src.domain import commands
from src.adapters import orm
from src.serivce_layer import messagebus, unit_of_work

orm.start_mappers()
router = APIRouter()


@router.post("/{username}", status_code=201)
def fetch_user(username: str) -> Any:
    """
    Fetch a single user by username
    """
    cmd = commands.CreateUser(username,
                              username,
                              username,
                              "a@a.a",
                              username,
                              username)

    uow = unit_of_work.UserUnitOfWork()
    messagebus.handle(cmd, uow)
    return 'OK'
