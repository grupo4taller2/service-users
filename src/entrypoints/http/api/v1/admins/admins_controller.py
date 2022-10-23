from fastapi import APIRouter, status
from src.adapters.repositories.unit_of_work import UnitOfWork

from src.entrypoints.http.api.v1.admins.req_res_admins_models import (
    AdminCreateRequest,
    AdminResponse
)

from src.domain import commands
from src.domain.admin import Admin
from src.serivce_layer import messagebus


router = APIRouter()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=AdminResponse
)
async def create_admin(req: AdminCreateRequest):
    cmd = commands.AdminCreateCommand(
        email=req.email
    )
    uow = UnitOfWork()
    admin: Admin = messagebus.handle(cmd, uow)[0]
    return AdminResponse(
        username=admin.username,
        first_name=admin.first_name,
        last_name=admin.last_name,
        email=admin.email
    )


@router.get(
    '/{email}',
    status_code=status.HTTP_200_OK,
    response_model=AdminResponse
)
async def get_admin(email: str):
    cmd = commands.AdminGetCommand(
        email=email
    )
    uow = UnitOfWork()
    admin: Admin = messagebus.handle(cmd, uow)[0]
    return AdminResponse(
        username=admin.username,
        first_name=admin.first_name,
        last_name=admin.last_name,
        email=admin.email
    )
