from src.domain.user import User
from src.domain.password import Password
from src.domain.password_encoder import NoEncoder


def test_user_creation():
    user = User(username='mateocalvo',
                first_name='Mateo',
                last_name='Calvo',
                email='macalvo@fi.uba.ar',
                password=Password(NoEncoder(), 'secret'),
                wallet='aaa111')
    assert user.username == 'mateocalvo'


def test_user_creation_with_empty_list_of_events():
    user = User(username='mateocalvo',
                first_name='Mateo',
                last_name='Calvo',
                email='macalvo@fi.uba.ar',
                password=Password(NoEncoder(), 'secret'),
                wallet='aaa111',
                events=[])
    assert user.username == 'mateocalvo'
