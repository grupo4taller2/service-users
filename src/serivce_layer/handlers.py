from src.conf.config import Settings

from src.domain.commands import (
    UserCreateCommand,
    UserGetCommand
)
from src.domain.events import (
    UserCreatedEvent
)

from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork

from src.domain.user import User
from src.domain.password import Password
from src.domain.password_encoder import ByCryptPasswordEncoder, CryptContext


def get_user(cmd: UserGetCommand, uow: AbstractUnitOfWork):
    # FIXME: THROW IF NOT EXISTS
    with uow:
        user = uow.repository.find_by_username(username=cmd.username)
        uow.commit()
        return user


def create_user(cmd: UserCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.repository.find_by_username(username=cmd.username)
        # FIXME: Throw if user exists
        if user is None:
            password = Password(ByCryptPasswordEncoder(
                CryptContext(schemes=Settings().CRYPT_CONTEXT_SCHEME,
                             deprecated=Settings().CRYPT_CONTEXT_DEPRECATED)),
                             cmd.password)

            user = User(
                username=cmd.username,
                first_name=cmd.first_name,
                last_name=cmd.last_name,
                email=cmd.email,
                password=password,
                wallet=cmd.wallet)
            uow.repository.save(user)
        uow.commit()
        return user


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUnitOfWork):
    print(f'Created event {event}')
