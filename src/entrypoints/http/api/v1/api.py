from fastapi import APIRouter

from src.entrypoints.http.api.v1 import (
    users_controller,
    riders_controller,
    drivers_controller,
    healthcheck
)

from src.entrypoints.http.api.v1.admins import admins_controller

api_router = APIRouter()

api_router.include_router(users_controller.router,
                          prefix="/users",
                          tags=["users"])

api_router.include_router(drivers_controller.router,
                          prefix='/drivers',
                          tags=['drivers'])

api_router.include_router(riders_controller.router,
                          prefix='/riders',
                          tags=['riders'])

api_router.include_router(admins_controller.router,
                          prefix='/admins',
                          tags=['admins'])

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
