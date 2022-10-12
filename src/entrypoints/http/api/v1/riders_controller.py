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
                         phone_number=rider.phone_number,
                         wallet=rider.wallet,
                         preferred_location_latitude=rider.location.latitude,
                         preferred_location_longitude=rider.location.longitude,
                         preferred_location_name=rider.location.name)


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
        phone_number=req.phone_number,
        wallet=req.wallet,
        preferred_location_latitude=req.preferred_location_latitude,
        preferred_location_longitude=req.preferred_location_longitude,
        preferred_location_name=req.preferred_location_name
    )
    uow = UnitOfWork()
    rider: Rider = messagebus.handle(cmd, uow)[0]
    return RiderResponse(username=rider.username,
                         email=rider.email,
                         first_name=rider.first_name,
                         last_name=rider.last_name,
                         phone_number=rider.email,
                         wallet=rider.wallet,
                         preferred_location_latitude=rider.location.latitude,
                         preferred_location_longitude=rider.location.longitude,
                         preferred_location_name=rider.location.name)
