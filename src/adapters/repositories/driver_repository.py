from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.adapters.repositories.base_repository import BaseRepository
from src.domain.user import User
from src.domain.driver import Driver
from src.domain.location import Location
from src.adapters.repositories.user_dto import UserDTO
from src.adapters.repositories.driver_dto import DriverDTO


class DriverRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    # FIXME: IDEM ABAJO, QUE LLEGUE ACA EL
    # CAR REPOSITORY CON LA MISMA SESSION PARA GUARDAR
    # EL AUTO DEL TIPO SI YA EXISTE.
    # A LO SUMO, SE VA A HACER UPDATE SI ALGO DEL AUTO
    # CAMBIÓ (PERO NO DEBERÏA PASAR)
    def save(self, rider: Driver):
        driver_dto = DriverDTO.from_entity(rider)
        # FIXME: Si no existe el user, crearlo. Rider tiene todos
        # los datos para insertar el user y el rider.
        try:
            self.session.add(driver_dto)
            self.seen.add(rider)
        except Exception:
            raise

    # FIXME: CarRepository tendría que llegar acá con
    # LA MISMA SESSION para que todo sea atómico
    def find_by_username(self, username: str) -> Driver:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(username=username).one()

            driver_dto: DriverDTO = self.session.query(DriverDTO) \
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
                      first_name=driver_dto.first_name,
                      last_name=driver_dto.last_name,
                      phone_number=driver_dto.phone_number,
                      wallet=driver_dto.wallet,
                      location=Location(driver_dto.preferred_latitude,
                                        driver_dto.preferred_longitude)
                      )
        self.seen.add(rider)
        return rider

    def find_by_email(self, email: str) -> User:
        raise NotImplementedError

    def find_by_email_or_username(self, email: str, username: str) -> User:
        raise NotImplementedError
