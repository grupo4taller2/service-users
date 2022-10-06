from fastapi import APIRouter

from src.entrypoints.http.api.v1 import (
    drivers_controller,
    healthcheck,
    users_controller
)


api_router = APIRouter()

api_router.include_router(users_controller.router,
                          prefix="/users",
                          tags=["users"])

api_router.include_router(drivers_controller.router,
                          prefix='/drivers',
                          tags=['drivers'])

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
