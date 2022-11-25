from fastapi import APIRouter

from src.webapi.v1.users import users_controller
from src.webapi.v1.riders import riders_controller
from src.webapi.v1.drivers import drivers_controller
from src.webapi.v1.admins import admins_controller
from src.webapi.v1.healthcheck import healthcheck
from src.webapi.v1.qualy_drivers import qualy_drivers
from src.webapi.v1.qualy_rider import qualy_rider
from src.webapi.v1.tokens import push_token

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


api_router.include_router(qualy_drivers.router,
                          prefix="/drivers",
                          tags=["qualy_driver"])


api_router.include_router(qualy_rider.router,
                          prefix="/riders",
                          tags=["qualy_rider"])

api_router.include_router(push_token.router,
                          prefix="/users",
                          tags=["token"])