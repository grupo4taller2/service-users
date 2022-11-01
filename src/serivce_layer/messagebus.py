from __future__ import annotations
import logging
from typing import List, Dict, Callable, Type, Union
from src.domain import commands, events
from . import handlers

from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork


logger = logging.getLogger(__name__)

Message = Union[commands.Command, events.Event]


def handle(
    message: Message,
    uow: AbstractUnitOfWork,
) -> List:
    results = []
    queue = [message]
    while queue:
        message = queue.pop(0)
        if isinstance(message, events.Event):
            handle_event(message, queue, uow)
        elif isinstance(message, commands.Command):
            cmd_result = handle_command(message, queue, uow)
            results.append(cmd_result)
        else:
            raise Exception(f"{message} was not an Event or Command")
    return results


def handle_event(
    event: events.Event,
    queue: List[Message],
    uow: AbstractUnitOfWork,
):
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug("handling event %s with handler %s", event, handler)
            handler(event, uow=uow)
            queue.extend(uow.collect_new_events())
        except Exception:
            logger.exception("Exception handling event %s", event)
            continue


def handle_command(
    command: commands.Command,
    queue: List[Message],
    uow: AbstractUnitOfWork,
):
    logger.debug("handling command %s", command)
    handler = COMMAND_HANDLERS[type(command)]
    result = handler(command, uow=uow)
    queue.extend(uow.collect_new_events())
    return result


EVENT_HANDLERS = {
    events.UserCreatedEvent: [handlers.publish_created_event],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.UserCreateCommand: handlers.create_user,
    commands.UserGetCommand: handlers.get_user,
    commands.UserSearchCommand: handlers.search_user,
    commands.UserGetAllCommand: handlers.get_all_users,

    commands.RiderCreateCommand: handlers.create_rider,
    commands.RiderGetCommand: handlers.get_rider,
    commands.RiderUpdateCommand: handlers.update_rider,

    commands.DriverCreateCommand: handlers.create_driver,
    commands.DriverGetCommand: handlers.get_driver,
    commands.DriverUpdateCommand: handlers.update_driver,

    commands.AdminCreateCommand: handlers.create_admin,
    commands.AdminGetCommand: handlers.get_admin,
}  # type: Dict[Type[commands.Command], Callable]
