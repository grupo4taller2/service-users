
from fastapi import APIRouter, status
from src.webapi.v1.qualy_passenger.req_res_qualy_passenger import (
    Passenger_qualy_create_request
)


from src.domain.passenger_qualification import Passenger_qualification
from src.repositories.unit_of_work_mongo import UnitOfWorkMongo
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


@router.get(
    "/{username}",
    status_code=status.HTTP_200_OK,
)
async def get_qualys_passenger(username: str):
    cmd = commands.PassengerQualyGetCommand(passenger_username=username)
    uow = UnitOfWorkMongo()
    driver_qualy = messagebus.handle(cmd, uow)[0]
    print(driver_qualy)
    return driver_qualy


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    # response_model=Driver_qualification_response
)
async def create_passenger(req: Passenger_qualy_create_request):
    cmd = commands.PassengerQualyCreateCommand(
        passenger_username=req.passenger_username,
        opinion=req.opinion,
        qualy=req.qualy,
        driver_username=req.driver_username,
    )
    uow = UnitOfWorkMongo()
    passenger_qualy: Passenger_qualification = messagebus.handle(cmd, uow)[0]
    return passenger_qualy


@router.get(
    "/average/{username}",
    status_code=status.HTTP_200_OK,
)
async def get_average_passenger(username: str):
    cmd = commands.PassengerQualyGetAverageCommand(passenger_username=username)
    uow = UnitOfWorkMongo()
    promedio = messagebus.handle(cmd, uow)[0]
    print(promedio)
    return promedio
