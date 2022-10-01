from fastapi import APIRouter

from src.entrypoints.http.api.v1 import users, healthcheck


api_router = APIRouter()

api_router.include_router(users.router,
                          prefix="/users",
                          tags=["users"])

api_router.include_router(healthcheck.router,
                          prefix="/healthcheck",
                          tags=["healthcheck"])
