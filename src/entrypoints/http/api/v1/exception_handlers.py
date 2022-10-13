from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from src.serivce_layer.exceptions import (
    DriverNotFoundException,
    UserNotFoundException
)


async def user_not_found_exception(
        request: Request,
        exc: UserNotFoundException) -> JSONResponse:

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