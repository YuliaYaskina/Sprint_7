import pytest
import requests
import urls
from helpers.data_generator import DataGenerate
import copy

@pytest.fixture
def data_generator():
    login = DataGenerate.generate_random_string(10)
    password = DataGenerate.generate_random_string(10)
    first_name = DataGenerate.generate_random_string(10)
    payload = {"login": login, "password": password, "firstName": first_name}
    return payload


@pytest.fixture
def courier(data_generator):
    payload = copy.copy(data_generator)
    requests.post(urls.URL_CREATE_COURIER, data=payload)
    yield payload

    payload_for_login = {"login": payload['login'], "password": payload['password']}
    response = requests.post(urls.URL_LOGIN, data=payload_for_login)
    courier_id = response.json()['id']

    requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

@pytest.fixture
def courier_auth(data_generator):
    create_payload = copy.copy(data_generator)
    requests.post(urls.URL_CREATE_COURIER, data=create_payload)

    payload_for_login = {"login": create_payload['login'], "password": create_payload['password']}
    response = requests.post(urls.URL_LOGIN, data=payload_for_login)
    courier_id = response.json()['id']
    create_payload['id'] = courier_id
    yield create_payload

    requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')


