from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.adapters.repositories.base_repository import UserBaseRepository
from src.domain.user import User
from src.adapters.repositories.user_dto import UserDTO


class UserRepository(UserBaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, user: User):
        user_dto = UserDTO.from_entity(user)
        try:
            self.session.add(user_dto)
            self.seen.add(user)
        except Exception:
            raise

    def find_by_username(self, username: str) -> User:
        try:
            user_dto = self.session.query(UserDTO) \
                .filter_by(username=username).one()
        except NoResultFound:
            return None
        except Exception:
            raise
        user = user_dto.to_entity()
        self.seen.add(user)
        return user

    def find_by_email(self, email: str) -> User:
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
