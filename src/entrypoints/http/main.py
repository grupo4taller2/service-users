
from fastapi import FastAPI, APIRouter
from src.conf.config import Settings
from src.entrypoints.http.api.v1 import api

from src.serivce_layer.exceptions import (
    DriverNotFoundException,
    UserNotFoundException
)

from src.entrypoints.http.api.v1.exception_handlers import (
    driver_not_found_exception,
    user_not_found_exception
)


root_router = APIRouter()
app = FastAPI(title="Users API", openapi_url="/openapi.json")

app.include_router(api.api_router, prefix=Settings().API_V1_STR)
app.include_router(root_router)

app.add_exception_handler(UserNotFoundException, user_not_found_exception)
app.add_exception_handler(DriverNotFoundException, driver_not_found_exception)
