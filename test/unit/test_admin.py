from src.domain.admin import Admin


def test_admin_creation():
    admin = Admin(
        username='mateoicalvo',
        first_name='mateo',
        last_name='calvo',
        email='mateo@calvo.com',
        blocked=False,
        events=[])
    assert admin is not None


def test_admin_equality():
    admin_1 = Admin(
        username='mateocalvo',
        first_name='mateo',
        last_name='calvo',
        email='mateo@calvo.com',
        blocked=False,
        events=[])

    admin_2 = Admin(
        username='mateocalvo',
        first_name='mateo',
        last_name='calvo',
        email='mateo@calvo.com',
        blocked=False,
        events=[])

    admin_3 = Admin(
        username='mateoicalvo',
        first_name='mateo',
        last_name='calvo',
        email='mateo@calvo.com',
        blocked=False,
        events=[])

    assert admin_1 == admin_2
    assert admin_2 != admin_3
    assert admin_1 != admin_3
