
from fastapi import APIRouter, status
from src.webapi.v1.qualy_rider.req_res_qualy_rider import (
    Rider_qualy_create_request
)


from src.domain.rider_qualification import Rider_qualification
from src.repositories.unit_of_work_mongo import UnitOfWorkMongo
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


@router.get(
    "/{username}/qualy",
    status_code=status.HTTP_200_OK,
)
async def get_qualys_rider(username: str):
    cmd = commands.RiderQualyGetCommand(rider_username=username)
    uow = UnitOfWorkMongo()
    driver_qualy = messagebus.handle(cmd, uow)[0]
    return driver_qualy


@router.post(
    "/qualy/create",
    status_code=status.HTTP_201_CREATED,
    # response_model=Driver_qualification_response
)
async def create_rider(req: Rider_qualy_create_request):
    cmd = commands.RiderQualyCreateCommand(
        rider_username=req.rider_username,
        opinion=req.opinion,
        qualy=req.qualy,
        driver_username=req.driver_username,
    )
    uow = UnitOfWorkMongo()
    rider_qualy: Rider_qualification = messagebus.handle(cmd, uow)[0]
    return rider_qualy


@router.get(
    "/{username}/qualy/average",
    status_code=status.HTTP_200_OK,
)
async def get_average_rider(username: str):
    cmd = commands.RiderQualyGetAverageCommand(rider_username=username)
    uow = UnitOfWorkMongo()
    promedio = messagebus.handle(cmd, uow)[0]
    return promedio
