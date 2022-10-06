from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
    event,
    func
)
from sqlalchemy.orm import registry, relationship


# FIXME: Add not null whenever required
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('username', String, unique=True, index=True),
    Column('email', String, unique=True, index=True),
    Column('hashed_password', String),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), server_default=func.now())
)

riders = Table(
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

drivers = Table(
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

admins = Table()

cars = Table(
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
    users_mapper = mapper()
    lines_mapper = mapper(model.OrderLine, order_lines)
    batches_mapper = mapper(
        model.Batch,
        batches,
        properties={
            "_allocations": relationship(
                lines_mapper,
                secondary=allocations,
                collection_class=set,
            )
        },
    )
    mapper(
        model.Product,
        products,
        properties={"batches": relationship(batches_mapper)},
    )


@event.listens_for(model.Product, "load")
def receive_load(product, _):
    product.events = []
