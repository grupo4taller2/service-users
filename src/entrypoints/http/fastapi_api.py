from fastapi import APIRouter, FastAPI
from typing import Any

from src.domain import commands
from src.serivce_layer import messagebus
from src.adapters.repositories.user_unit_of_work import UserUnitOfWork

router = APIRouter(tags=['users'])
app = FastAPI(title="Users API", openapi_url="/openapi.json")
app.include_router(router)

@router.post("/asd/{username}", status_code=201)
def fetch_user(username: str) -> Any:
    """
    Fetch a single user by username
    """
    cmd = commands.UserCreateCommand(username,
                              username,
                              username,
                              "a@a.a",
                              username,
                              username)

    uow = UserUnitOfWork()
    messagebus.handle(cmd, uow)
    return 'OK'

router2 = APIRouter(tags=["health"])


@router2.get(
    '/health')
async def health():
    return 'Todo muy bien por aqui'

@router2.post("/health/{new_username}", status_code=201)
def fetch_user(new_username: str) -> Any:
    """
    Fetch a single user by username
    """
    cmd = commands.UserCreateCommand(
        username=new_username,
        first_name='ElNombre',
        last_name='ElApellido',
        email='email@test.com',
        password='SuperSecret',
        wallet='la_wallet'
        )

    uow = UserUnitOfWork()
    messagebus.handle(cmd, uow)
    return 'OK'


app.include_router(router2)
