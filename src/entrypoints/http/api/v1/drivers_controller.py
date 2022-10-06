from fastapi import APIRouter, status
from src.entrypoints.http.api.v1.req_res_drivers_models \
    import DriverCreatedResponse, DriverCreateRequest

from src.domain import commands


router = APIRouter()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=DriverCreatedResponse
)
async def create_driver(req: DriverCreateRequest):
    cmd = commands.DriverCreateCommand(
        username=req.username,
        first_name=req.first_name,
        last_name=req.last_name,
        email=req.email,
        password=req.password,
        wallet=req.wallet,
        phone_number=req.phone_number,
        preferred_latitude=req.preferred_latitude,
        preferred_longitude=req.preferred_longitude,
        car_name=req.car_name,
        car_year_of_production=req.car_year_of_production,
        car_color=req.car_color,
        car_plate=req.car_plate
    )
    uow = DriverUnitOfWork()
    driver = messagebus.handle(cmd, uow)[0]
    return DriverCreatedResponse(
        
    )