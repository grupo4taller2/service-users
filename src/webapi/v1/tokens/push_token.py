
from fastapi import APIRouter, status
from src.webapi.v1.tokens.req_res_push_token import (Push_token_creation)


# from src.domain.push_token import Push_token
from src.repositories.unit_of_work_mongo import UnitOfWorkMongo
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


@router.post(
    "/push/token",
    status_code=status.HTTP_201_CREATED,
    # response_model=Driver_qualification_response
)
async def create_push_token(req: Push_token_creation):
    cmd = commands.PushTokenCreateCommand(
        username=req.username,
        token=req.token
    )
    uow = UnitOfWorkMongo()
    push_token = messagebus.handle(cmd, uow)[0]
    return push_token
