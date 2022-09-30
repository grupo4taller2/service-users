from __future__ import annotations
from typing import TYPE_CHECKING
from src.domain import commands, events
from src.domain.user import User


if TYPE_CHECKING:
    from . import unit_of_work


def create_user(
    cmd: commands.CreateUser,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        user = uow.users.find_by_username(username=cmd.username)
        if user is None:
            user = User(cmd.username,
                        cmd.first_name,
                        cmd.last_name,
                        cmd.email,
                        cmd.password,
                        cmd.wallet)
            uow.users.save(user)
        uow.commit()


def publish_created_event(
    event: events.Created,
    uow: unit_of_work.AbstractUnitOfWork,
):
    print(f'Created event {event}')
