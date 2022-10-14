from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.serivce_layer.exceptions import UserNotFoundException

from src.adapters.repositories.base_repository import BaseRepository
from src.domain.user import User
from src.database.user_dto import UserDTO


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
        
        #query = self.session.query(UserDTO)
        #query = query.filter(UserDTO.username.ilike(f'%{like}%')).limit(2)
        
        try:
            # user_dtos = self.session.query(UserDTO).filter(UserDTO.username.ilike(f'%{like}%')).all()
            user_dtos = self.session.query(UserDTO)
            user_dtos = user_dtos.filter(UserDTO.username.ilike(f'%{like}%')).all()
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
