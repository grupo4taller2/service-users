from fastapi import APIRouter, status

from src.domain.rider import Rider
from src.repositories.unit_of_work import UnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

from src.webapi.v1.riders.req_res_riders_models import (
    RiderCreateRequest,
    RiderResponse,
    RiderUpdateRequest,

)

router = APIRouter()


@router.get(
    '/{email}',
    status_code=status.HTTP_200_OK,
    response_model=RiderResponse
)
async def get_rider(email: str):
    cmd = commands.RiderGetCommand(
        email=email
    )
    uow = UnitOfWork()
    rider: Rider = messagebus.handle(cmd, uow)[0]
    return RiderResponse(username=rider.username,
                         email=rider.email,
                         first_name=rider.first_name,
                         last_name=rider.last_name,
                         phone_number=rider.phone_number,
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
                         preferred_location_latitude=rider.location.latitude,
                         preferred_location_longitude=rider.location.longitude,
                         preferred_location_name=rider.location.name)


@router.patch(
    '/{email}/status',
    response_model=RiderResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_rider_status(email: str, req: RiderUpdateRequest):
    cmd = commands.RiderUpdateCommand(
        email=email,
        first_name=req.first_name,
        last_name=req.last_name,
        phone_number=req.phone_number,
        preferred_location_latitude=req.preferred_location_latitude,
        preferred_location_longitude=req.preferred_location_longitude,
        preferred_location_name=req.preferred_location_name
    )
    uow = UnitOfWork()
    rider: Rider = messagebus.handle(cmd, uow)[0]
    return RiderResponse(
        username=rider.username,
        email=rider.email,
        first_name=rider.first_name,
        last_name=rider.last_name,
        phone_number=rider.phone_number,
        preferred_location_latitude=rider.location.latitude,
        preferred_location_longitude=rider.location.longitude,
        preferred_location_name=rider.location.name)
