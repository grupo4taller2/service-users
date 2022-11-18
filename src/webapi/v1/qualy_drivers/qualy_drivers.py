
from fastapi.responses import JSONResponse

from fastapi import APIRouter, status
from src.webapi.v1.qualy_drivers.req_res_qualy_driver import (
    Driver_qualy_create_request,
)


from src.domain.driver_qualification import Driver_qualification
from src.repositories.unit_of_work_mongo import UnitOfWorkMongo
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


@router.get(
    "/{username}/qualy",
    status_code=status.HTTP_200_OK,
)
async def get_qualys_driver(username: str):
    cmd = commands.DriverQualyGetCommand(driver_username=username)
    uow = UnitOfWorkMongo()
    driver_qualy = messagebus.handle(cmd, uow)[0]
    return driver_qualy


@router.post(
    "/qualy/create",
    status_code=status.HTTP_201_CREATED,
    # response_model=Driver_qualification_response
)
async def create_driver(req: Driver_qualy_create_request):
    print(req.qualy)
    if (req.qualy > 5):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=str("Qualy puntation is over 5")
        )
    if (req.qualy < 0):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=str("Qualy puntation is under 0")
        )
    cmd = commands.DriverQualyCreateCommand(
        rider_username=req.rider_username,
        opinion=req.opinion,
        qualy=req.qualy,
        driver_username=req.driver_username,
    )
    uow = UnitOfWorkMongo()
    driver_qualy: Driver_qualification = messagebus.handle(cmd, uow)[0]
    return driver_qualy


@router.get(
    "/{username}/qualy/average",
    status_code=status.HTTP_200_OK,
)
async def get_average_driver(username: str):
    cmd = commands.DriverQualyGetAverageCommand(driver_username=username)
    uow = UnitOfWorkMongo()
    promedio = messagebus.handle(cmd, uow)[0]
    return promedio
