from behave import given, when, then
from src.conf.config import Settings


@given(u'There are {:d} drivers')
def step_add_n_drivers(context, n_drivers):
    for i in range(n_drivers):
        response = context.client.post(
            Settings().API_V1_STR + '/drivers',
            json={
                "username": f'driver_{i}',
                "first_name": "fname",
                "last_name": "lname",
                "email": f'thedriver{i}@domain.com',
                "password": "secret",
                "wallet": "wallet",
                "phone_number": "123456789",
                "prefered_latitude": -34.612580,
                "preferred_longitude": -58.408061,
                "car_name": "Toyota Corolla",
                "car_year_of_production": 2009,
                "color": "red",
                "plate": "AAA 123"
                }
        )
        assert response.status_code == 201


@when(u'I create a driver with username "{username}"')
def step_create_driver(context, username):
    response = context.client.post(
            Settings().API_V1_STR + '/drivers',
            json={
                "username": f'{username}',
                "first_name": "fname",
                "last_name": "lname",
                "email": f'{username}@test.com',
                "password": "secret",
                "wallet": "wallet",
                "phone_number": "123456789",
                "preferred_latitude": -34.612580,
                "preferred_longitude": -58.408061,
                "car_name": "Toyota Corolla",
                "car_year_of_production": 2009,
                "car_color": "red",
                "car_plate": "AAA 123"
                }
        )
    assert response.status_code == 201


@then(u'The driver "{driver_username}" exists in the platform')
def step_fetch_driver(context, driver_username):
    response = context.client.get(
        f'{Settings().API_V1_STR}/drivers/{driver_username}'
    )
    assert response.json()['username'] == driver_username
