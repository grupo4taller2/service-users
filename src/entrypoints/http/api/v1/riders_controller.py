from fastapi import APIRouter, status

from src.domain.rider import Rider
from src.adapters.repositories.unit_of_work import UnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

from src.entrypoints.http.api.v1.req_res_riders_models import (
    RiderCreateRequest,
    RiderResponse,
)

router = APIRouter()


@router.get(
    '/{a_username}',
    status_code=status.HTTP_200_OK,
    response_model=RiderResponse
)
async def get_rider(a_username: str):
    cmd = commands.RiderGetCommand(
        username=a_username
    )
    uow = UnitOfWork()
    rider: Rider = messagebus.handle(cmd, uow)[0]
    return RiderResponse(username=rider.username,
                         email=rider.email,
                         first_name=rider.first_name,
                         last_name=rider.last_name,
                         phone_number=rider.email,
                         wallet=rider.wallet,
                         preferred_latitude=rider.location.latitude,
                         preferred_longitude=rider.location.longitude)


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=RiderResponse
)
async def create_rider(req: RiderCreateRequest):
    cmd = commands.RiderCreateCommand(
        username=req.username,
        first_name=req.first_name,
        last_name=req.last_name,
        email=req.email,
        password=req.password,
        phone_number=req.phone_number,
        wallet=req.wallet,
        preferred_latitude=req.preferred_latitude,
        preferred_longitude=req.preferred_longitude
    )
    uow = UnitOfWork()
    rider: Rider = messagebus.handle(cmd, uow)[0]
    return RiderResponse(username=rider.username,
                         email=rider.email,
                         first_name=rider.first_name,
                         last_name=rider.last_name,
                         phone_number=rider.email,
                         wallet=rider.wallet,
                         preferred_latitude=rider.location.latitude,
                         preferred_longitude=rider.location.longitude)
