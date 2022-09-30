import abc
from src.domain.user import User
from typing import Set


class UserBaseRepository(metaclass=abc.ABCMeta):
    def __init__(self):
        self.seen: Set[User] = set()

    @abc.abstractmethod
    def save(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_username(self, username: str) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_email(self, email: str) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_email_or_username(self, email: str, username: str) -> User:
        raise NotImplementedError

    # @abc.abstractmethod
    # def all(self, q: Optional[str], offset: int, limit: int) -> List[User]:
    #    raise NotImplementedError

    # @abc.abstractmethod
    # def total(self) -> int:
    #    raise NotImplementedError

    # @abc.abstractmethod
    # def update(self, user: User):
    #    raise NotImplementedError
