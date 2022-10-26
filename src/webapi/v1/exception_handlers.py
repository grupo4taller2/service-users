from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from src.serivce_layer.exceptions import (
    DriverNotFoundException,
    RiderNotFoundException,
    UserNotFoundException,
    AdminNotFoundException
)


async def user_not_found_exception(
        request: Request,
        exc: UserNotFoundException) -> JSONResponse:

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=str(exc)
    )


async def rider_not_found_exception(
        request: Request,
        exc: RiderNotFoundException) -> JSONResponse:

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=str(exc)
    )


async def driver_not_found_exception(
        request: Request,
        exc: DriverNotFoundException) -> JSONResponse:

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=str(exc)
    )


async def admin_not_found_exception(
        request: Request,
        exc: AdminNotFoundException) -> JSONResponse:

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=str(exc)
    )
