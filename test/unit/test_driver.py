from src.domain.driver import Driver
from src.domain.car import Car
from src.domain.location import Location
from src.domain.password import Password
from src.domain.password_encoder import NoEncoder


def test_user_creation():
    driver = Driver(username='mateocalvo',
                    first_name='Mateo',
                    last_name='Calvo',
                    email='macalvo@fi.uba.ar',
                    password=Password(NoEncoder(), 'secret'),
                    wallet='aaa111',
                    phone_number='123456789',
                    location=Location(-34.544879, -58.451024),
                    car=Car(name='Toyota Corolla',
                            year_of_production=2009,
                            color='red',
                            plate='AAA 123')
                    )

    assert driver.username == 'mateocalvo'


def test_driver_creation_with_empty_list_of_events():
    driver = Driver(username='mateocalvo',
                    first_name='Mateo',
                    last_name='Calvo',
                    email='macalvo@fi.uba.ar',
                    password=Password(NoEncoder(), 'secret'),
                    wallet='aaa111',
                    phone_number='123456789',
                    location=Location(-34.544879, -58.451024),
                    car=Car(name='Toyota Corolla',
                            year_of_production=2009,
                            color='red',
                            plate='AAA 123'),
                    events=[]
                    )

    assert driver.username == 'mateocalvo'
