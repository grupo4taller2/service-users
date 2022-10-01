from behave import given, when, then
from src.conf.config import Settings


@given(u'There are {:d} users')
def step_add_n_users(context, n_users):
    for i in range(n_users):
        context.client.post(
            Settings().API_V1_STR + '/users',
            json={
                "username": f'user_{i}',
                "first_name": "fname",
                "last_name": "lname",
                "email": f'theuser{i}@domain.com',
                "password": "secret",
                "wallet": "wallet"
                }
        )


@when(u'I create the user "{}"')
def step_create_user(context, username):
    context.client.post(
        Settings().API_V1_STR + '/users',
        json={
            "username": f'{username}',
            "first_name": "fname",
            "last_name": "lname",
            "email": f'{username}@test.com',
            "password": "secret",
            "wallet": "wallet"
            }
    )


@then(u'The user "{}" exists in the platform')
def step_impl(context, username):
    response = context.client.get(
        f'{Settings().API_V1_STR}/users/{username}'
    )
    assert response.json()['username'] == username
