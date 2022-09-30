from dataclasses import dataclass


class Event:
    pass


@dataclass
class Created(Event):
    username: str
    email: str
