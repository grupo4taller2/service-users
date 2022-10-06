from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.adapters.repositories.base_repository import BaseRepository
from src.domain.user import User
from src.domain.rider import Rider
from src.domain.location import Location
from src.adapters.repositories.user_dto import UserDTO
from src.adapters.repositories.rider_dto import RiderDTO


class RiderRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, rider: Rider):
        rider_dto = RiderDTO.from_entity(rider)
        # FIXME: Si no existe el user, crearlo. Rider tiene todos
        # los datos para insertar el user y el rider.
        try:
            self.session.add(rider_dto)
            self.seen.add(rider)
        except Exception:
            raise

    def find_by_username(self, username: str) -> Rider:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(username=username).one()

            rider_dto: RiderDTO = self.session.query(RiderDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            return None
        except Exception:
            raise
        user = user_dto.to_entity()
        # FIXME: Crear rider a partir de un user existente?
        rider = Rider(username=user.username,
                      email=user.email,
                      password=user.password,
                      events=[],
                      first_name=rider_dto.first_name,
                      last_name=rider_dto.last_name,
                      phone_number=rider_dto.phone_number,
                      wallet=rider_dto.wallet,
                      location=Location(rider_dto.preferred_latitude,
                                        rider_dto.preferred_longitude)
                      )
        self.seen.add(rider)
        return rider

    def find_by_email(self, email: str) -> User:
        raise NotImplementedError
        try:
            user_dto = self.session.query(UserDTO) \
                .filter_by(email=email).one()
        except NoResultFound:
            return None
        except Exception:
            raise
        user = user_dto.to_entity()
        self.seen.add(user)
        return user

    def find_by_email_or_username(self, email: str, username: str) -> User:
        raise NotImplementedError
        try:
            user_dto = self.session.query(UserDTO) \
                .filter((UserDTO.email == email)
                        | (UserDTO.username == username)).one()
        except NoResultFound:
            return None
        except Exception:
            raise
        user = user_dto.to_entity()
        self.seen.add(user)
        return user
