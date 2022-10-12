from fastapi import APIRouter, status
from src.entrypoints.http.api.v1.req_res_drivers_models \
    import DriverResponse, DriverCreateRequest

from src.domain.driver import Driver
from src.adapters.repositories.unit_of_work import UnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


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
        wallet=req.wallet,
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
        wallet=driver.wallet,
        preferred_location_latitude=driver.location.latitude,
        preferred_location_longitude=driver.location.longitude,
        preferred_location_name=driver.location.name,
        car_manufacturer=driver.car.manufacturer,
        car_model=driver.car.model,
        car_year_of_production=driver.car.year_of_production,
        car_color=driver.car.color,
        car_plate=driver.car.plate
    )
