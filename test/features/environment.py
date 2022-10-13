from src.entrypoints.http.main import app
from behave import fixture, use_fixture
# import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.conf import config

Session = sessionmaker(bind=create_engine(config.Settings().DATABASE_URI))
session = Session()


class Rider:
    pass


# Crea una variable para poder hacer llamadas a la API
@fixture
def app_client(context, *args, **kwargs):
    context.client = TestClient(app)
    yield context.client

# Hooks para hacer Rollbacks y setear variable de entorno de test
# def before_all(context):
#    os.environ["TEST_MODE"] = "1"


def before_feature(context, feature):
    use_fixture(app_client, context)
    session.execute('TRUNCATE TABLE cars, drivers, riders, users CASCADE;')
    session.commit()
    # Rollback de variables (permite compartir variables entre steps)
    context.vars = {}
    context.vars['chosen_rider'] = Rider()
    # context.client.post("/reset")

# def after_scenario(context, scenario):
#    context.client.post("/reset")


def after_all(context):
    session.close()
