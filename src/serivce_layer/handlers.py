from src.domain.commands import (
    UserCreateCommand
)
from src.domain.events import (
    UserCreatedEvent
)

from src.serivce_layer.abstract_unit_of_work import AbstractUserUnitOfWork

from src.domain.user import User


def create_user(cmd: UserCreateCommand, uow: AbstractUserUnitOfWork):
    with uow:
        user = uow.repository.find_by_username(username=cmd.username)
        if user is None:
            user = User(cmd.username,
                        cmd.first_name,
                        cmd.last_name,
                        cmd.email,
                        cmd.password,
                        cmd.wallet)
            uow.repository.save(user)
        uow.commit()


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUserUnitOfWork):
    print(f'Created event {event}')
