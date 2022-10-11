from src.conf.config import Settings

from src.domain.commands import (
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
from src.domain.password import Password
from src.domain.password_encoder import ByCryptPasswordEncoder, CryptContext


def _create_password(plain_text: str):
    return Password(ByCryptPasswordEncoder(
                CryptContext(schemes=Settings().CRYPT_CONTEXT_SCHEME,
                             deprecated=Settings().CRYPT_CONTEXT_DEPRECATED)),
                    plain_text)


def get_user(cmd: UserGetCommand, uow: AbstractUnitOfWork):
    # FIXME: THROW IF NOT EXISTS
    with uow:
        user = uow.user_repository.find_by_username(username=cmd.username)
        uow.commit()
        return user


def create_user(cmd: UserCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.user_repository.find_by_username(username=cmd.username)
        # FIXME: Throw if user exists
        if user is None:
            password = _create_password(cmd.password)

            user = User(
                username=cmd.username,
                email=cmd.email,
                password=password)
            uow.user_repository.save(user)
        uow.commit()
        return user


def get_rider(cmd: RiderGetCommand, uow: AbstractUnitOfWork):
    raise Exception


def create_rider(cmd: RiderCreateCommand, uow: AbstractUnitOfWork):
    password = _create_password(cmd.password)
    location = Location(float(cmd.preferred_latitude),
                        float(cmd.preferred_longitude),
                        cmd.preferred_location)
    with uow:
        # FIXME: Fijarse que no exista, handlear bien
        user = uow.user_repository.find_by_username(username=cmd.username)
        if user is None:

            user = User(
                username=cmd.username,
                email=cmd.email,
                password=password)
            uow.user_repository.save(user)
            # uow.commit()
        rider = uow.rider_repository.find_by_username(username=cmd.username)
        if rider is not None:
            return rider
        rider = Rider(
            username=cmd.username,
            email=cmd.email,
            password=password,
            first_name=cmd.first_name,
            last_name=cmd.last_name,
            phone_number=cmd.phone_number,
            wallet=cmd.wallet,
            location=location
        )
        uow.rider_repository.save(rider)
        uow.commit()
        return rider


def create_driver(cmd: DriverCreateCommand, uow: AbstractUnitOfWork):
    password = _create_password(cmd.password)
    location = Location(float(cmd.preferred_latitude),
                        float(cmd.preferred_longitude),
                        cmd.preferred_location)
    with uow:
        # FIXME: Fijarse que no exista, handlear bien
        user = uow.user_repository.find_by_username(username=cmd.username)
        if user is None:

            user = User(
                username=cmd.username,
                email=cmd.email,
                password=password)
            uow.user_repository.save(user)
            # uow.commit()
        driver = uow.driver_repository.find_by_username(username=cmd.username)
        if driver is not None:
            return driver

        car = Car(
            plate=cmd.car_plate,
            manufacturer=cmd.car_manufacturer,
            model=cmd.car_model,
            year_of_production=cmd.car_year_of_production,
            color=cmd.car_color
        )

        driver = Driver(
            username=cmd.username,
            email=cmd.email,
            password=password,
            first_name=cmd.first_name,
            last_name=cmd.last_name,
            phone_number=cmd.phone_number,
            wallet=cmd.wallet,
            location=location,
            car=car
        )
        uow.driver_repository.save(driver)
        uow.commit()
        return driver


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUnitOfWork):
    print(f'Created event {event}')
