from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.adapters.repositories.base_repository import UserBaseRepository
from src.domain.user import User


class UserRepository(UserBaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, user: User):
        try:
            self.session.add(user)
            self.seen.add(user)
        except Exception:
            raise

    def find_by_username(self, username: str) -> User:
        try:
            user = self.session.query(User).filter_by(username=username).one()
            self.seen.add(user)
        except NoResultFound:
            return None
        except Exception:
            raise
        return user

    def find_by_email(self, email: str) -> User:
        try:
            user = self.session.query(User).filter_by(email=email).one()
            self.seen.add(user)
        except NoResultFound:
            return None
        except Exception:
            raise
        return user

    def find_by_email_or_username(self, email: str, username: str) -> User:
        try:
            user = self.session.query(User) \
                .filter(
                    (User.email == email) | (User.username == username)
                    ).one()
            self.seen.add(user)
        except NoResultFound:
            return None
        except Exception:
            raise
        return user
