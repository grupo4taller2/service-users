import abc
from passlib.context import CryptContext


class PasswordEncoder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def encode(self, password: str) -> str:
        raise NotImplementedError()


class ByCryptPasswordEncoder(PasswordEncoder):
    def __init__(self, pwd_context: CryptContext):
        self.pwd_context = pwd_context

    def encode(self, password: str) -> str:
        return self.pwd_context.hash(password)

class NoEncoder(PasswordEncoder):
    def encode(self, password: str) -> str:
        return password
