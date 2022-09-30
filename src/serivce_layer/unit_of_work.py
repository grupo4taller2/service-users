from __future__ import annotations

import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.adapters.repositories.base_repository import UserBaseRepository
from src.adapters.repositories.user_repository import UserRepository

from src.conf import config


class AbstractUnitOfWork(abc.ABC):
    users: UserBaseRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def collect_new_events(self):
        for user in self.users.seen:
            while user.events:
                yield user.events.pop(0)

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.Settings().DATABASE_URI,
        isolation_level="REPEATABLE READ",
    )
)


class UserUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.users = UserRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
