from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.serivce_layer.exceptions import (
    RiderNotFoundException,
    UserNotFoundException
)

from src.adapters.repositories.base_repository import BaseRepository
from src.domain.rider import Rider
from src.domain.location import Location
from src.database.user_dto import UserDTO
from src.database.rider_dto import RiderDTO


class RiderRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, rider: Rider):
        rider_dto = RiderDTO.from_entity(rider)
        try:
            self.session.add(rider_dto)
            self.seen.add(rider)
        except IntegrityError:
            user_dto = UserDTO.from_entity(rider)
            self.session.add(user_dto)
            self.session.flush()
            self.session.add(rider_dto)
        except Exception:
            raise

    def find_by_username(self, username: str) -> Rider:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise UserNotFoundException(f'User {username} not found')

        try:
            rider_dto: RiderDTO = self.session.query(RiderDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise RiderNotFoundException(f'Rider {username} not found')

        location: Location = Location(rider_dto.preferred_location_latitude,
                                      rider_dto.preferred_location_longitude,
                                      rider_dto.preferred_location_name)

        rider = Rider(username=user_dto.username,
                      first_name=user_dto.first_name,
                      last_name=user_dto.last_name,
                      email=user_dto.email,
                      blocked=user_dto.blocked,
                      events=[],
                      phone_number=rider_dto.phone_number,
                      wallet=rider_dto.wallet,
                      location=location
                      )

        self.seen.add(rider)
        return rider

    def find_by_email(self, email: str) -> Rider:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(email=email).one()
        except NoResultFound:
            raise UserNotFoundException(email)

        try:
            rider_dto: RiderDTO = self.session.query(RiderDTO) \
                .filter_by(username=user_dto.username).one()
        except NoResultFound:
            raise RiderNotFoundException(user_dto.username)

        location: Location = Location(rider_dto.preferred_location_latitude,
                                      rider_dto.preferred_location_longitude,
                                      rider_dto.preferred_location_name)

        rider = Rider(username=user_dto.username,
                      first_name=user_dto.first_name,
                      last_name=user_dto.last_name,
                      email=user_dto.email,
                      blocked=user_dto.blocked,
                      events=[],
                      phone_number=rider_dto.phone_number,
                      wallet=rider_dto.wallet,
                      location=location
                      )

        self.seen.add(rider)
        return rider

    def find_by_email_or_username(self, email: str, username: str) -> Rider:
        try:
            user_dto = self.session.query(UserDTO) \
                .filter((UserDTO.email == email)
                        | (UserDTO.username == username)).one()
        except NoResultFound:
            raise UserNotFoundException(username)
        except Exception:
            raise

        try:
            rider_dto: RiderDTO = self.session.query(RiderDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise RiderNotFoundException(username)

        location: Location = Location(rider_dto.preferred_location_latitude,
                                      rider_dto.preferred_location_longitude,
                                      rider_dto.preferred_location_name)

        rider = Rider(username=user_dto.username,
                      first_name=user_dto.first_name,
                      last_name=user_dto.last_name,
                      email=user_dto.email,
                      blocked=user_dto.blocked,
                      events=[],
                      phone_number=rider_dto.phone_number,
                      wallet=rider_dto.wallet,
                      location=location
                      )

        self.seen.add(rider)
        return rider

    def update(self, rider: Rider) -> Rider:
        rider_dto = RiderDTO.from_entity(rider)
        user_attrs_update = {
            UserDTO.first_name: rider.first_name,
            UserDTO.last_name: rider.last_name
        }
        rider_attrs_update = {
            RiderDTO.phone_number: rider.phone_number,
            RiderDTO.wallet: rider.wallet,
            RiderDTO.preferred_location_latitude: rider.location.latitude,
            RiderDTO.preferred_location_longitude: rider.location.longitude,
            RiderDTO.preferred_location_name: rider.location.name
        }
        try:
            self.session.query(UserDTO).filter_by(username=rider.username) \
                .update(user_attrs_update)
            self.session.query(RiderDTO).filter_by(username=rider.username) \
                .update(rider_attrs_update)
            self.seen.add(rider)
        except IntegrityError:
            raise RiderNotFoundException(rider_dto.username)
        except Exception as e:
            raise e
        return rider
