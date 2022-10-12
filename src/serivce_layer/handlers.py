from src.domain.commands import (
    Command,
    DriverCreateCommand,
    RiderCreateCommand,
    RiderGetCommand,
    UserCreateCommand,
    UserGetCommand
)
from src.domain.events import (
    UserCreatedEvent
)

from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork

from src.domain.user import User
from src.domain.rider import Rider
from src.domain.driver import Driver
from src.domain.car import Car
from src.domain.location import Location


def _user_from_cmd(cmd: Command) -> User:
    return User(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[]
    )


def _location_from_cmd(cmd: Command) -> Location:
    return Location(
        cmd.preferred_location_latitude,
        cmd.preferred_location_longitude,
        cmd.preferred_location_name
    )


def _car_from_cmd(cmd: Command) -> Car:
    return Car(
        plate=cmd.car_plate,
        manufacturer=cmd.car_manufacturer,
        model=cmd.car_model,
        year_of_production=cmd.car_year_of_production,
        color=cmd.car_color
        )


def _rider_from_cmd(cmd: Command) -> Rider:
    return Rider(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[],
        phone_number=cmd.phone_number,
        wallet=cmd.wallet,
        location=_location_from_cmd(cmd)
    )


def _driver_from_cmd(cmd: Command) -> Driver:
    return Driver(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[],
        phone_number=cmd.phone_number,
        wallet=cmd.wallet,
        location=_location_from_cmd(cmd),
        car=_car_from_cmd(cmd)
    )


def get_user(cmd: UserGetCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.user_repository.find_by_username(username=cmd.username)
        uow.commit()
        return user


def create_user(cmd: UserCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        uow.commit()
        return user


def get_rider(cmd: RiderGetCommand, uow: AbstractUnitOfWork):
    raise Exception


def create_rider(cmd: RiderCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        rider = _rider_from_cmd(cmd)
        uow.rider_repository.save(rider)
        uow.commit()
        return rider


def create_driver(cmd: DriverCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        # FIXME: Fijarse que no exista, handlear bien
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        driver = _driver_from_cmd(cmd)
        uow.driver_repository.save(driver)
        uow.commit()
        return driver


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUnitOfWork):
    print(f'Created event {event}')
