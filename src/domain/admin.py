from src.domain import user


class Admin(user.User):

    def __hash__(self):
        return hash(self.username)

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            return False
        return self.username == other.username
