from src.domain.user import User


def test_user_creation():
    user = User(username='mateocalvo',
                first_name='Mateo',
                last_name='Calvo',
                blocked=False,
                email='macalvo@fi.uba.ar')
    assert user.username == 'mateocalvo'


def test_user_creation_with_empty_list_of_events():
    user = User(username='mateocalvo',
                first_name='Mateo',
                last_name='Calvo',
                email='macalvo@fi.uba.ar',
                blocked=False,
                events=[])
    assert user.username == 'mateocalvo'


def test_user_equality_only_with_username():
    user_one = User(username='mateocalvo',
                    first_name='Mateo',
                    last_name='Calvo',
                    email='macalvo@fi.uba.ar',
                    blocked=False,
                    events=[])

    user_two = User(username='mateocalvo',
                    first_name='oetaM',
                    last_name='ovlaC',
                    blocked=False,
                    email='ovlacam@fi.uba.ar',
                    events=[])

    assert user_one == user_two
