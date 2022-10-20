from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.serivce_layer.exceptions import (
    CarNotFoundException,
    DriverNotFoundException,
    UserNotFoundException
)

from src.adapters.repositories.base_repository import BaseRepository
from src.domain.user import User
from src.domain.driver import Driver
from src.domain.location import Location
from src.database.user_dto import UserDTO
from src.database.driver_dto import DriverDTO
from src.database.car_dto import CarDTO


class DriverRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, driver: Driver):
        driver_dto = DriverDTO.from_entity(driver)
        car_dto = CarDTO.from_entity(driver, driver.car)
        try:
            self.session.add(driver_dto)
            self.session.flush()
            self.session.add(car_dto)
        except IntegrityError:
            user_dto = UserDTO.from_entity(driver)
            self.session.add(user_dto)
            self.session.flush()
            self.session.add(driver_dto)
            self.session.flush()
            self.session.add(car_dto)
        except Exception:
            raise

    def find_by_username(self, username: str) -> Driver:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise UserNotFoundException(username)

        try:
            driver_dto: DriverDTO = self.session.query(DriverDTO) \
                .filter_by(username=username).one()

        except NoResultFound:
            raise DriverNotFoundException(username)

        try:
            car_dto: CarDTO = self.session.query(CarDTO) \
                .filter_by(driver_username=username).first()
        except NoResultFound:
            raise CarNotFoundException(f'No car for driver{username}')
        except Exception:
            raise

        location = Location(driver_dto.preferred_location_latitude,
                            driver_dto.preferred_location_longitude,
                            driver_dto.preferred_location_name)

        driver = Driver(username=user_dto.username,
                        first_name=user_dto.first_name,
                        last_name=user_dto.last_name,
                        email=user_dto.email,
                        blocked=user_dto.blocked,
                        events=[],
                        phone_number=driver_dto.phone_number,
                        wallet=driver_dto.wallet,
                        location=location,
                        car=car_dto.to_entity())
        self.seen.add(driver)
        return driver

    def find_by_email(self, email: str) -> Driver:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(email=email).one()
        except NoResultFound:
            raise UserNotFoundException(email)

        try:
            driver_dto: DriverDTO = self.session.query(DriverDTO) \
                .filter_by(username=user_dto.username).one()
        except NoResultFound:
            raise DriverNotFoundException(user_dto.username)

        try:
            car_dto: CarDTO = self.session.query(CarDTO) \
                .filter_by(driver_username=user_dto.username).first()
        except NoResultFound:
            raise CarNotFoundException(f'No car for driver{user_dto.username}')
        except Exception:
            raise

        location: Location = Location(driver_dto.preferred_location_latitude,
                                      driver_dto.preferred_location_longitude,
                                      driver_dto.preferred_location_name)

        driver = Driver(username=user_dto.username,
                        first_name=user_dto.first_name,
                        last_name=user_dto.last_name,
                        email=user_dto.email,
                        blocked=user_dto.blocked,
                        events=[],
                        phone_number=driver_dto.phone_number,
                        wallet=driver_dto.wallet,
                        location=location,
                        car=car_dto.to_entity()
                        )
        self.seen.add(driver)
        return driver

    def update(self, driver: Driver) -> Driver:
        driver_dto = DriverDTO.from_entity(driver)
        user_attrs_update = {
            UserDTO.first_name: driver.first_name,
            UserDTO.last_name: driver.last_name
        }
        driver_attrs_update = {
            DriverDTO.phone_number: driver.phone_number,
            DriverDTO.wallet: driver.wallet,
            DriverDTO.preferred_location_latitude: driver.location.latitude,
            DriverDTO.preferred_location_longitude: driver.location.longitude,
            DriverDTO.preferred_location_name: driver.location.name
        }
        try:
            self.session.query(UserDTO).filter_by(username=driver.username) \
                .update(user_attrs_update)
            self.session.query(DriverDTO).filter_by(username=driver.username) \
                .update(driver_attrs_update)
            self.seen.add(driver)
        except IntegrityError:
            raise DriverNotFoundException(driver_dto.username)
        except Exception as e:
            raise e
        return driver

    def find_by_email_or_username(self, email: str, username: str) -> User:
        raise NotImplementedError
