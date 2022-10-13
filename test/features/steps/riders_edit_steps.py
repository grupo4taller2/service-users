from behave import given, when, then
from src.conf.config import Settings


@given(u'I choose "{username}" for username')
def step_choose_username(context, username):
    context.vars["chosen_rider"].username = username


@given(u'I choose "{fname}" for first name')
def step_choose_first_name(context, fname):
    context.vars["chosen_rider"].first_name = fname


@given(u'I choose "{lname}" for last name')
def step_choose_last_name(context, lname):
    context.vars["chosen_rider"].last_name = lname


@given(u'I choose "{some_email}" for email')
def step_choose_email(context, some_email):
    context.vars["chosen_rider"].email = some_email


@given(u'I choose "{some_phone_number}" for phone number')
def step_choose_phone_number(context, some_phone_number):
    context.vars["chosen_rider"].phone_number = some_phone_number


@given(u'I choose "{a_wallet}" for wallet')
def step_choose_wallet(context, a_wallet):
    context.vars["chosen_rider"].wallet = a_wallet


@given(u'I choose {:f} as preferred location latitude')
def step_choose_preferred_location_latitude(context, latitude):
    context.vars["chosen_rider"].preferred_location_latitude = latitude


@given(u'I choose {:f} as preferred location longitude')
def step_choose_preferred_location_longitude(context, longitude):
    context.vars["chosen_rider"].preferred_location_longitude = longitude


@given(u'I choose "{some_place}" as preferred location name')
def step_choose_preferred_location_name(context, some_place):
    context.vars["chosen_rider"].preferred_location_name = some_place


@given(u'I register as a rider')
def step_register_as_rider_with_chosen_args(context):
    rider = context.vars['chosen_rider']
    req_body = {
        "username": rider.username,
        "first_name": rider.first_name,
        "last_name": rider.last_name,
        "email": rider.email,
        "wallet": rider.wallet,
        "phone_number": rider.phone_number,
        "preferred_location_latitude": rider.preferred_location_latitude,
        "preferred_location_longitude": rider.preferred_location_longitude,
        "preferred_location_name": rider.preferred_location_name,
    }
    response = context.client.post(
        Settings().API_V1_STR + '/riders',
        json=req_body,
    )
    assert response.status_code == 201


@when(u'I change the first name of rider with email "{email}" to "{new_name}"')
def step_change_rider_first_name(context, email, new_name):
    response = context.client.patch(
        Settings().API_V1_STR + f'/riders/{email}/status',
        json={
            "first_name": new_name
        }
    )
    assert response.status_code == 202


@then(u'The first name of rider with email "{email}" is updated to "{name}"')
def step_check_rider_first_name_changed(context, email, name):
    response = context.client.get(
        f'{Settings().API_V1_STR}/users/{email}'
    )
    assert response.status_code == 200
    assert response.json()['first_name'] == name
