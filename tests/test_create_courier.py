import requests
import urls
from conftest import courier
from conftest import data_generator
import allure
import copy

class TestCourierCreation:
    @allure.title('Проверка создания курьера ')
    @allure.description('Создается новый курьер и проверяется статус-код')
    def test_courier_creation_status_code(self, data_generator):
        payload = copy.copy(data_generator)
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 201

        payload = {"login": data_generator["login"], "password": data_generator["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        courier_id = response.json()['id']

        requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

    @allure.title('Проверка статус-кода при попытке создания двух одинаковых курьеров')
    @allure.description('Два раза создаются курьеры с одинаковыми данными и проверяется статус-код')
    def test_existing_courier_statuse_code(self,courier):
        payload = copy.copy(courier)
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409

    @allure.title('Проверка текста ошибки при попытке создания двух одинаковых курьеров')
    @allure.description('Два раза создаются курьеры с одинаковыми данными и проверяется текст полученной ошибки')
    def test_existing_courier_error_message(self, courier):
        payload = copy.copy(courier)
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка статус-кода при попытке создать курьера с незаполненным логином')
    @allure.description('В поле логин передается пустое значение и проверяется статус-код')
    def test_no_login_status_code(self, data_generator):
        payload = copy.copy(data_generator)
        payload['login'] = ''
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка текста ошибки при попытке создать курьера с незаполненным логином')
    @allure.description('В поле логин передается пустое значение и проверяется текст ошибки')
    def test_no_login_error_message(self, data_generator):
        payload = copy.copy(data_generator)
        payload['login'] = ''
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка статус-кода при попытке создать курьера с незаполненным паролем')
    @allure.description('В поле пароль передается пустое значение и проверяется статус-код')
    def test_no_password_status_code(self, data_generator):
        payload = copy.copy(data_generator)
        payload['password'] = ''
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка текста ошибки при попытке создать курьера с незаполненным паролем')
    @allure.description('В поле пароль передается пустое значение и проверяется текст ошибки')
    def test_no_password_error_message(self, data_generator):
        payload = copy.copy(data_generator)
        payload['password'] = ''
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка статус-кода при попытке создать курьера с незаполненным именем')
    @allure.description('В поле firstName передается пустое значение и проверяется статус-код ответа')
    def test_no_firstName_status_code(self, data_generator):
        payload = copy.copy(data_generator)
        payload['firstName'] = ''
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 201

        payload_for_login = {"login": payload['login'], "password": payload['password']}
        response = requests.post(urls.URL_LOGIN, data=payload_for_login)
        courier_id = response.json()['id']

        requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

    @allure.title('Проверка текста ответа при успешном создании курьера')
    @allure.description('Создается новый курьер и проверяется текст ответа')
    def test_response_text_success(self, data_generator):
        payload = copy.copy(data_generator)
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.text == '{"ok":true}'

        payload_for_login = {"login": payload['login'], "password": payload['password']}
        response = requests.post(urls.URL_LOGIN, data=payload_for_login)
        courier_id = response.json()['id']

        requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

    @allure.title('Проверка статус-кода при попытке создать курьера с уже занятым логином')
    @allure.description('Происходит попытка создания нового курьера и проверяется статус-код')
    def test_same_login_status_code(self, data_generator, courier):
        payload = copy.copy(data_generator)
        payload['login'] = courier["login"]
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409

    @allure.title('Проверка текста ошибки при попытке создать курьера с уже занятым логином')
    @allure.description('Происходит попытка создания нового курьера и проверяется текст ошибки')
    def test_same_login_error_message(self, data_generator, courier):
        payload = copy.copy(data_generator)
        payload['login'] = courier["login"]
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."












