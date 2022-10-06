from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
    func
)
from sqlalchemy.orm import registry

from src.adapters.repositories import (
    user_dto,
    rider_dto
)


mapper_registry = registry()
metadata = mapper_registry.metadata
# FIXME: Add not null whenever required

users_table = Table(
    'users',
    metadata,
    Column('username', String, unique=True, index=True),
    Column('email', String, unique=True, index=True),
    Column('hashed_password', String),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), server_default=func.now())
)

riders_table = Table(
    'riders',
    metadata,
    Column('username', ForeignKey('users.username')),
    Column('first_name', String),
    Column('last_name', String),
    Column('phone_number', String),
    Column('wallet', String),
    Column('preferred_longitude', Float),
    Column('preferred_latitude', Float),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), server_default=func.now())
)

drivers_table = Table(
    'drivers',
    metadata,
    Column('username', ForeignKey('users.username')),
    Column('first_name', String),
    Column('last_name', String),
    Column('phone_number', String),
    Column('wallet', String),
    Column('preferred_longitude', Float),
    Column('preferred_latitude', Float),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), server_default=func.now())
)

admins_table = Table()

cars_table = Table(
    'cars',
    metadata,
    Column('username', ForeignKey('users.username'), primary_key=True),
    Column('plate', String, primary_key=True),
    Column('manufacturer', String),
    Column('model', String),
    Column('year_of_production', Integer),
)

# TODO: ubicaciones predeterminadas de cada user aca?


def start_mappers():
    mapper_registry.map_imperatively(user_dto.UserDTO, users_table)
    mapper_registry.map_imperatively(rider_dto.RiderDTO, riders_table)
