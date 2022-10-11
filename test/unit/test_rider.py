from src.domain.rider import Rider
from src.domain.location import Location
from src.domain.password import Password
from src.domain.password_encoder import NoEncoder


def test_rider_creation():
    rider = Rider(username='mateocalvo',
                  first_name='Mateo',
                  last_name='Calvo',
                  email='macalvo@fi.uba.ar',
                  password=Password(NoEncoder(), 'secret'),
                  wallet='aaa111',
                  phone_number='123456789',
                  location=Location(-34.544879, -58.451024, 'El Monumental')
                  )

    assert rider.username == 'mateocalvo'


def test_rider_creation_with_empty_list_of_events():
    rider = Rider(username='mateocalvo',
                  first_name='Mateo',
                  last_name='Calvo',
                  email='macalvo@fi.uba.ar',
                  password=Password(NoEncoder(), 'secret'),
                  wallet='aaa111',
                  phone_number='123456789',
                  location=Location(-34.544879, -58.451024, 'El Monumental'),
                  events=[]
                  )

    assert rider.username == 'mateocalvo'


def test_rider_equality():
    rider_one = Rider(username='mateocalvo',
                      first_name='Mateo',
                      last_name='Calvo',
                      email='macalvo@fi.uba.ar',
                      password=Password(NoEncoder(), 'secret'),
                      wallet='aaa111',
                      phone_number='123456789',
                      location=Location(-34.544879, -58.451024,
                                        'El Monumental'),
                      )

    rider_two = Rider(username='mateocalvo',
                      first_name='Some Awesome Name',
                      last_name='James',
                      email='lebronjames@fi.uba.ar',
                      password=Password(NoEncoder(), 'secret'),
                      wallet='aaa111',
                      phone_number='123456789',
                      location=Location(-34.544879, -58.451024,
                                        'El Monumental'),
                      events=[]
                      )

    assert rider_one == rider_two
