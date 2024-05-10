import pytest
import requests
import urls
from helpers.data_generator import DataGenerate


@pytest.fixture
def courier():
    login = DataGenerate.generate_random_string(10)
    password = DataGenerate.generate_random_string(10)
    first_name = DataGenerate.generate_random_string(10)
    payload = {"login": login, "password": password, "firstName": first_name}
    requests.post(urls.URL_CREATE_COURIER, data=payload)
    yield payload

    payload = {"login": login, "password": password}
    response = requests.post(urls.URL_LOGIN, data=payload)
    courier_id = response.json()['id']

    requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

@pytest.fixture
def courier_auth():
    login = DataGenerate.generate_random_string(10)
    password = DataGenerate.generate_random_string(10)
    first_name = DataGenerate.generate_random_string(10)
    create_payload = {"login": login, "password": password, "firstName": first_name}
    requests.post(urls.URL_CREATE_COURIER, data=create_payload)

    payload = {"login": login, "password": password}
    response = requests.post(urls.URL_LOGIN, data=payload)
    courier_id = response.json()['id']
    create_payload['id'] = courier_id
    yield create_payload

    requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')


