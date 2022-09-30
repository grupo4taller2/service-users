from dataclasses import dataclass


class Command:
    pass


@dataclass
class CreateUser(Command):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    wallet: str
