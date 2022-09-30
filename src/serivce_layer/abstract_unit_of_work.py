from __future__ import annotations

import abc
from src.adapters.repositories.base_repository import UserBaseRepository


class AbstractUserUnitOfWork(abc.ABC):
    repository: UserBaseRepository

    def __enter__(self) -> AbstractUserUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def collect_new_events(self):
        for user in self.repository.seen:
            while user.events:
                yield user.events.pop(0)

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
