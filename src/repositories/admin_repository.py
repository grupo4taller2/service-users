from psycopg2 import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.domain.user import User
from src.serivce_layer.exceptions import (
    UserNotFoundException,
    AdminNotFoundException
)

from src.repositories.base_repository import BaseRepository
from src.domain.admin import Admin
from src.database.user_dto import UserDTO
from src.database.admin_dto import AdminDTO


class AdminRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, admin: Admin):
        admin_dto = AdminDTO.from_entity(admin)
        try:
            self.session.add(admin_dto)
            self.seen.add(admin)
        except IntegrityError:
            user_dto = UserDTO.from_entity(admin)
            self.session.add(user_dto)
            self.session.flush()
            self.session.add(admin_dto)
        except Exception:
            raise

    def find_by_username(self, username: str) -> Admin:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise UserNotFoundException(username)
        try:
            admin_dto: AdminDTO = self.session.query(AdminDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise AdminNotFoundException(f'Admin {username} not found')

        admin = Admin(admin_dto.username,
                      user_dto.last_name,
                      user_dto.email,
                      user_dto.blocked,
                      events=[])
        self.seen.add(admin)
        return admin

    def find_by_email(self, email: str) -> User:
        try:
            user_dto: UserDTO = self.session.query(UserDTO) \
                .filter_by(email=email).one()
        except NoResultFound:
            raise UserNotFoundException(email)
        try:
            username = user_dto.username
            admin_dto: AdminDTO = self.session.query(AdminDTO) \
                .filter_by(username=user_dto.username).one()
        except NoResultFound:
            raise AdminNotFoundException(f'Admin {username} not found')

        admin = Admin(username=admin_dto.username,
                      first_name=user_dto.first_name,
                      last_name=user_dto.last_name,
                      email=user_dto.email,
                      blocked=user_dto.blocked,
                      events=[])
        self.seen.add(admin)
        return admin

    def find_by_email_or_username(self, email: str, username: str) -> User:
        raise NotImplementedError

    def update(self, admin: Admin) -> Admin:
        raise NotImplementedError
