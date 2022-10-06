from fastapi import APIRouter, status

from src.adapters.repositories.unit_of_work import UnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

from src.entrypoints.http.api.v1.req_res_users_models import (
    UserRequest,
    UserResponse,
)

router = APIRouter()


@router.get(
    '/{a_username}',
    status_code=status.HTTP_200_OK,
    response_model=UserResponse
)
async def get_user(a_username: str):
    cmd = commands.UserGetCommand(
        username=a_username
    )
    uow = UnitOfWork()
    user = messagebus.handle(cmd, uow)[0]
    return UserResponse(username=user.username,
                        email=user.email)


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
async def create_user(req: UserRequest):
    cmd = commands.UserCreateCommand(
        username=req.username,
        email=req.email,
        password=req.password
    )
    uow = UnitOfWork()
    user = messagebus.handle(cmd, uow)[0]
    return UserResponse(username=user.username,
                        email=user.email)
