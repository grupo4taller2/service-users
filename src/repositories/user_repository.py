from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.serivce_layer.exceptions import UserNotFoundException

from src.repositories.base_repository import BaseRepository
from src.domain.user import User
from src.database.user_dto import UserDTO


def round_down_to_nearest_multiple_of(offset, limit, n_pages):
    for i in range(0, n_pages):
        current_multiple = i * limit
        next_multiple = (i + 1) * limit
        if offset >= current_multiple and offset < next_multiple:
            return current_multiple
    return 0


class UserRepository(BaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, user: User):
        user_dto = UserDTO.from_entity(user)
        try:
            self.session.add(user_dto)
            self.session.flush()
            self.seen.add(user)
        except Exception:
            raise

    def find_by_username(self, username: str) -> User:
        try:
            user_dto = self.session.query(UserDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            raise UserNotFoundException(username)
        except Exception:
            raise
        user = user_dto.to_entity()
        self.seen.add(user)
        return user

    def search_by_username_like(self, like: str) -> User:
        try:
            user_dtos = self.session.query(UserDTO)
            user_dtos = \
                user_dtos.filter(UserDTO.username.ilike(f'%{like}%')).all()
        except NoResultFound:
            raise UserNotFoundException(like)
        except Exception:
            raise
        found_users = []

        for udto in user_dtos:
            user = udto.to_entity()
            self.seen.add(user)
            found_users.append(user)
        return found_users

    def find_by_email(self, email: str) -> User:
        try:
            user_dto = self.session.query(UserDTO) \
                .filter_by(email=email).one()
        except NoResultFound:
            raise UserNotFoundException(email)
        except Exception:
            raise
        user = user_dto.to_entity()
        self.seen.add(user)
        return user

    def find_by_email_or_username(self, email: str, username: str) -> User:
        try:
            user_dto = self.session.query(UserDTO) \
                .filter((UserDTO.email == email)
                        | (UserDTO.username == username)).one()
        except NoResultFound:
            raise UserNotFoundException(username)
        except Exception:
            raise
        user = user_dto.to_entity()
        self.seen.add(user)
        return user

    def update(self, user: User) -> User:
        raise NotImplementedError

    def all(self, username_like: str, offset: int, limit: int):
        user_dtos = self.session.query(UserDTO)
        if username_like is not None:
            user_dtos = user_dtos.filter(
                UserDTO.username.ilike(f'%{username_like}%'))

        total_users = user_dtos.count()
        total_pages = (total_users // limit) + 1*(total_users % limit != 0)
        offset = round_down_to_nearest_multiple_of(offset, limit, total_pages)
        current_page = (offset // limit) + 1

        user_dtos = user_dtos.limit(limit).offset(offset)
        found_users = []
        for u_dto in user_dtos:
            user = u_dto.to_entity()
            self.seen.add(user)
            found_users.append(user)
        return current_page, total_pages, found_users
