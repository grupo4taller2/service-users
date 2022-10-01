from fastapi import APIRouter, HTTPException, status

from src.adapters.repositories.user_unit_of_work import UserUnitOfWork
from src.domain import commands
from src.serivce_layer import messagebus

router = APIRouter()


@router.post("/{username}",
             status_code=status.HTTP_201_CREATED)
def create_user(username: str):
    cmd = commands.UserCreateCommand(
        username=username,
        first_name='ElNombre',
        last_name='ElApellido',
        email='email@test.com',
        password='SuperSecret',
        wallet='la_wallet'
    )
    uow = UserUnitOfWork()
    results = messagebus.handle(cmd, uow)
    if not results:
        raise HTTPException(
            status_code=404, detail=f"User {username} not found"
        )
    return results
