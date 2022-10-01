from src.domain.commands import (
    UserCreateCommand,
    UserGetCommand
)
from src.domain.events import (
    UserCreatedEvent
)

from src.serivce_layer.abstract_unit_of_work import AbstractUserUnitOfWork

from src.domain.user import User
from src.domain.password import Password
from src.domain.password_encoder import ByCryptPasswordEncoder, CryptContext


def get_user(cmd: UserGetCommand, uow: AbstractUserUnitOfWork):
    # FIXME: THROW IF NOT EXISTS
    with uow:
        user = uow.repository.find_by_username(username=cmd.username)
        uow.commit()
        return user


def create_user(cmd: UserCreateCommand, uow: AbstractUserUnitOfWork):
    with uow:
        user = uow.repository.find_by_username(username=cmd.username)
        # FIXME: Throw if user exists
        if user is None:
            user = User(
                username=cmd.username,
                first_name=cmd.first_name,
                last_name=cmd.last_name,
                email=cmd.email,
                password=Password(
                    ByCryptPasswordEncoder(
                        CryptContext(schemes=["bcrypt"],
                                     deprecated="auto")),
                    cmd.password),
                wallet=cmd.wallet)
            uow.repository.save(user)
        uow.commit()
        return user


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUserUnitOfWork):
    print(f'Created event {event}')
