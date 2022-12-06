from behave import given, when, then
from src.conf.config import Settings
from fastapi.testclient import TestClient


def create_user(context, name):
    req_body = {
        "username": name,
        "first_name": name,
        "last_name": name,
        "email": f'{name}@domain.com',
        "phone_number": '123456',
        "preferred_location_latitude": -33.0,
        "preferred_location_longitude": -54.0,
        "preferred_location_name": 'oslo',
    }
    response = context.client.post(
        Settings().API_V1_STR + '/riders',
        json=req_body,
    )
    assert response.status_code == 201


@given(u'existen {:d} usuarios registrados')
def step_impl(context, n_usuarios):
    for i in range(n_usuarios):
        name = f'user_{i}'
        create_user(context, name)


@when(u'obtengo los usuarios con offset {:d} limit {:d}')
def step_impl_obtencion_usuarios(context, offset, limit):
    client: TestClient = context.client
    params = {
        'offset': offset,
        'limit': limit
    }
    response = client.get(
        Settings().API_V1_STR + '/users/',
        params=params
    )
    assert response.status_code == 200
    context.vars['obtained_page'] = response.json()


@then(u'el numero de pagina actual es {:d}')
def step_impl_pagina_acutal(context, pagina_actual_esperada):
    pagina_actual_obtenida = context.vars['obtained_page'].get('actual_page')
    assert pagina_actual_obtenida == pagina_actual_esperada


@then(u'el numero de paginas totales es {:d}')
def step_impl_paginas_totales(context, n_pages):
    obtenidas = context.vars['obtained_page'].get('total_pages')
    assert obtenidas == n_pages


@then(u'los usuarios desde {:d} hasta {:d} estan en la pagina actual')
def step_impl_usuarios_contenidos(context, first_user, last_user):
    all_usernames = [
        user['username'] for user in context.vars['obtained_page'].get('users')
    ]
    for u in range(first_user, last_user + 1):
        username = f'user_{u}'
        assert username in all_usernames


@then(u'la pagina actual tiene {:d} usuarios')
def step_impl_comparacion_cantidad_users(context, n_users):
    obtained_users = len(context.vars['obtained_page'].get('users'))
    assert obtained_users == n_users
