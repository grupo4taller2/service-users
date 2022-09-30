from typing import Optional, List
from pydantic import BaseModel, EmailStr


class User:
    def __init__(self, username, first_name, last_name, email, password, wallet):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = password
        self.wallet = wallet
        self.events = []
