from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.adapters.repositories.driver_repository import DriverRepository
from src.conf import config

from src.adapters.repositories.user_repository import UserRepository
from src.adapters.repositories.admin_repository import AdminRepository
from src.adapters.repositories.rider_repository import RiderRepository
from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork


# UserDTO.__table__.create(bind=engine, checkfirst=True)

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.Settings().DATABASE_URI,
        isolation_level="REPEATABLE READ",
    )
)


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.user_repository = UserRepository(self.session)
        self.rider_repository = RiderRepository(self.session)
        self.driver_repository = DriverRepository(self.session)
        self.admin_repository = AdminRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
