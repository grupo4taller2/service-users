from fastapi import APIRouter, status
from src.entrypoints.http.api.v1.req_res_drivers_models \
    import DriverCreatedResponse, DriverCreateRequest

router = APIRouter()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=DriverCreatedResponse
)
async def create_driver(req: DriverCreateRequest):
    raise NotImplementedError
