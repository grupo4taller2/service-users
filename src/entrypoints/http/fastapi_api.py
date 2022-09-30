from fastapi import APIRouter, FastAPI
from typing import Any

from src.domain import commands
from src.adapters import orm
from src.serivce_layer import messagebus, unit_of_work

orm.start_mappers()
router = APIRouter(tags=['users'])
app = FastAPI(title="Users API", openapi_url="/openapi.json")
app.include_router(router)

@router.post("/asd/{username}", status_code=201)
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

router2 = APIRouter(tags=["health"])


@router2.get(
    '/health')
async def health():
    return 'OsssK'

@router2.post("/health/{username}", status_code=201)
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


app.include_router(router2)
