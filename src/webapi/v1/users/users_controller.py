from typing import List
from fastapi import APIRouter, status

from src.repositories.unit_of_work import UnitOfWork
from src.domain import commands
from src.domain.user import User
from src.serivce_layer import messagebus

from src.webapi.v1.users.req_res_users_models import (
    UserCreateRequest,
    UserResponse
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
    user: User = messagebus.handle(cmd, uow)[0]
    return UserResponse(username=user.username,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email)


@router.get(
    '/search/{username_like}',
    status_code=status.HTTP_200_OK,
    response_model=List[UserResponse]
)
async def search_user(username_like: str):
    cmd = commands.UserSearchCommand(
        username_like=username_like
    )
    uow = UnitOfWork()
    users: List[User] = messagebus.handle(cmd, uow)[0]
    return [
        UserResponse(username=u.username,
                     first_name=u.first_name,
                     last_name=u.last_name,
                     email=u.email)
        for u in users
    ]


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
async def create_user(req: UserCreateRequest):
    cmd = commands.UserCreateCommand(
        username=req.username,
        first_name=req.first_name,
        last_name=req.last_name,
        email=req.email,
    )
    uow = UnitOfWork()
    user = messagebus.handle(cmd, uow)[0]
    return UserResponse(username=user.username,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email)
