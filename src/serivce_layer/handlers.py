from src.domain.commands import (
    Command,
    DriverCreateCommand,
    DriverGetCommand,
    RiderCreateCommand,
    RiderGetCommand,
    RiderUpdateCommand,
    UserCreateCommand,
    UserGetCommand,
    UserSearchCommand
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
        user = uow.user_repository.find_by_email_or_username(
            username=cmd.username,
            email=cmd.username)
        uow.commit()
        return user


def search_user(cmd: UserSearchCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.user_repository.search_by_username_like(
            like=cmd.username_like
        )
        uow.commit()
        return user


def create_user(cmd: UserCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        uow.commit()
        return user


def get_rider(cmd: RiderGetCommand, uow: AbstractUnitOfWork):
    with uow:
        rider = uow.rider_repository.find_by_email_or_username(
            cmd.email,
            cmd.username)
        uow.commit()
        return rider


def create_rider(cmd: RiderCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        rider = _rider_from_cmd(cmd)
        uow.rider_repository.save(rider)
        uow.commit()
        return rider


def update_rider(cmd: RiderUpdateCommand, uow: AbstractUnitOfWork):
    with uow:
        rider: Rider = uow.rider_repository.find_by_email(cmd.email)
        if cmd.first_name:
            rider.first_name = cmd.first_name
        if cmd.last_name:
            rider.last_name = cmd.last_name
        if cmd.phone_number:
            rider.phone_number = cmd.phone_number
        if cmd.wallet:
            rider.wallet = cmd.wallet
        loc_name = cmd.preferred_location_name
        loc_lat = cmd.preferred_location_latitude
        loc_long = cmd.preferred_location_longitude
        if loc_name and loc_lat and loc_long:
            rider.location = Location(loc_lat, loc_long, loc_name)
        updated_rider = uow.rider_repository.update(rider)
        uow.commit()
        return updated_rider


def create_driver(cmd: DriverCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        # FIXME: Fijarse que no exista, handlear bien
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        driver = _driver_from_cmd(cmd)
        uow.driver_repository.save(driver)
        uow.commit()
        return driver


def get_driver(cmd: DriverGetCommand, uow: AbstractUnitOfWork):
    with uow:
        driver = uow.driver_repository.find_by_username(cmd.username)
        uow.commit()
        return driver


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUnitOfWork):
    print(f'Created event {event}')
