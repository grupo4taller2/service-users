from behave import given, when, then


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


@given(u'I choose -34.0 as preferred location latitude')
def step_choose_preferred_location_latitude(context):
    raise NotImplementedError


@given(u'I choose -34.0 as preferred location longitude')
def step_choose_preferred_location_longitude(context):
    raise NotImplementedError


@given(u'I choose "some name" as preferred location name')
def step_choose_preferred_location_name(context):
    raise NotImplementedError


@given(u'I register as a rider')
def step_register_as_rider_with_chosen_args(context):
    raise NotImplementedError


@when(u'I change my first name to "mateo"')
def step_change_rider_first_name(context):
    raise NotImplementedError


@then(u'My first name is updated to "mateo"')
def step_check_rider_first_name_changed(context):
    raise NotImplementedError
