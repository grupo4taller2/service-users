from fastapi import APIRouter, status

from src.webapi.v1.drivers.req_res_drivers_models import (
    DriverCreateRequest,
    DriverResponse,
    DriverUpdateRequest
)

from src.domain.driver import Driver
from src.repositories.unit_of_work import UnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


@router.get(
    '/{email}',
    status_code=status.HTTP_200_OK,
    response_model=DriverResponse
)
async def get_driver(email: str):
    cmd = commands.DriverGetCommand(
        email=email
    )
    uow = UnitOfWork()
    driver: Driver = messagebus.handle(cmd, uow)[0]
    return DriverResponse(
        username=driver.username,
        email=driver.email,
        first_name=driver.first_name,
        last_name=driver.last_name,
        phone_number=driver.phone_number,
        preferred_location_latitude=driver.location.latitude,
        preferred_location_longitude=driver.location.longitude,
        preferred_location_name=driver.location.name,
        car_manufacturer=driver.car.manufacturer,
        car_model=driver.car.model,
        car_year_of_production=driver.car.year_of_production,
        car_color=driver.car.color,
        car_plate=driver.car.plate)


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=DriverResponse
)
async def create_driver(req: DriverCreateRequest):
    cmd = commands.DriverCreateCommand(
        username=req.username,
        first_name=req.first_name,
        last_name=req.last_name,
        email=req.email,
        phone_number=req.phone_number,
        preferred_location_latitude=req.preferred_location_latitude,
        preferred_location_longitude=req.preferred_location_longitude,
        preferred_location_name=req.preferred_location_name,
        car_manufacturer=req.car_manufacturer,
        car_model=req.car_model,
        car_year_of_production=req.car_year_of_production,
        car_color=req.car_color,
        car_plate=req.car_plate
    )
    uow = UnitOfWork()
    driver: Driver = messagebus.handle(cmd, uow)[0]
    return DriverResponse(
        username=driver.username,
        first_name=driver.first_name,
        last_name=driver.last_name,
        email=driver.email,
        phone_number=driver.phone_number,
        preferred_location_latitude=driver.location.latitude,
        preferred_location_longitude=driver.location.longitude,
        preferred_location_name=driver.location.name,
        car_manufacturer=driver.car.manufacturer,
        car_model=driver.car.model,
        car_year_of_production=driver.car.year_of_production,
        car_color=driver.car.color,
        car_plate=driver.car.plate
    )


@router.patch(
    '/{email}/status',
    response_model=DriverResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_driver_status(email: str, req: DriverUpdateRequest):
    cmd = commands.DriverUpdateCommand(
        email=email,
        first_name=req.first_name,
        last_name=req.last_name,
        phone_number=req.phone_number,
        preferred_location_latitude=req.preferred_location_latitude,
        preferred_location_longitude=req.preferred_location_longitude,
        preferred_location_name=req.preferred_location_name,
        car_manufacturer=req.car_manufacturer,
        car_model=req.car_model,
        car_year_of_production=req.car_year_of_production,
        car_color=req.car_color,
        car_plate=req.car_plate
    )
    uow = UnitOfWork()
    driver: Driver = messagebus.handle(cmd, uow)[0]
    return DriverResponse(
        username=driver.username,
        email=driver.email,
        first_name=driver.first_name,
        last_name=driver.last_name,
        phone_number=driver.phone_number,
        preferred_location_latitude=driver.location.latitude,
        preferred_location_longitude=driver.location.longitude,
        preferred_location_name=driver.location.name,
        car_manufacturer=driver.car.manufacturer,
        car_model=driver.car.model,
        car_year_of_production=driver.car.year_of_production,
        car_color=driver.car.color,
        car_plate=driver.car.plate)


@router.get(
    '/username/all',
    status_code=status.HTTP_200_OK,
)
async def get_drivers():
    cmd = commands.DriverGetAllCommand(
        cantidad=10
    )
    uow = UnitOfWork()
    driver_list = messagebus.handle(cmd, uow)[0]
    return driver_list
