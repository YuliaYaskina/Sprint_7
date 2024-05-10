import requests
import urls
from helpers.data_generator import DataGenerate
from conftest import courier
import allure

class TestCourierCreation:
    @allure.title('Проверка создания курьера')
    @allure.description('Создается новый курьер и проверяется статус-код')
    def test_courier_creation_status_code(self):
        login = DataGenerate.generate_random_string(10)
        password = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 201

        payload = {"login": login, "password": password}
        response = requests.post(urls.URL_LOGIN, data=payload)
        courier_id = response.json()['id']

        requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

    @allure.title('Проверка статус-кода при попытке создания двух одинаковых курьеров')
    @allure.description('Два раза создаются курьеры с одинаковыми данными и проверяется статус-код')
    def test_existing_courier_statuse_code(self,courier):
        payload = {"login": courier["login"], "password": courier["password"], "firstName": courier["firstName"]}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409

    @allure.title('Проверка текста ошибки при попытке создания двух одинаковых курьеров')
    @allure.description('Два раза создаются курьеры с одинаковыми данными и проверяется текст полученной ошибки')
    def test_existing_courier_error_message(self, courier):
        payload = {"login": courier["login"], "password": courier["password"], "firstName": courier["firstName"]}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка статус-кода при попытке создать курьера с незаполненным логином')
    @allure.description('В поле логин передается пустое значение и проверяется статус-код')
    def test_no_login_status_code(self):
        password = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"password": password, "firstName": first_name, "login": ""}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка текста ошибки при попытке создать курьера с незаполненным логином')
    @allure.description('В поле логин передается пустое значение и проверяется текст ошибки')
    def test_no_login_error_message(self):
        password = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"password": password, "firstName": first_name, "login": ""}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка статус-кода при попытке создать курьера с незаполненным паролем')
    @allure.description('В поле пароль передается пустое значение и проверяется статус-код')
    def test_no_password_status_code(self):
        login = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"login": login, "firstName": first_name, "password":""}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка текста ошибки при попытке создать курьера с незаполненным паролем')
    @allure.description('В поле пароль передается пустое значение и проверяется текст ошибки')
    def test_no_password_error_message(self):
        login = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"login": login, "firstName": first_name, "password":""}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка статус-кода при попытке создать курьера с незаполненным именем')
    @allure.description('В поле firstName передается пустое значение и проверяется статус-код ответа')
    def test_no_firstName_status_code(self):
        login = DataGenerate.generate_random_string(10)
        password = DataGenerate.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": ""}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 201

        payload = {"login": login, "password": password}
        response = requests.post(urls.URL_LOGIN, data=payload)
        courier_id = response.json()['id']

        requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

    @allure.title('Проверка текста ответа при успешном создании курьера')
    @allure.description('Создается новый курьер и проверяется текст ответа')
    def test_response_text_success(self,courier):
        login = DataGenerate.generate_random_string(10)
        password = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.text == '{"ok":true}'

        payload = {"login": login, "password": password}
        response = requests.post(urls.URL_LOGIN, data=payload)
        courier_id = response.json()['id']

        requests.delete(f'{urls.URL_DELETE_COURIER}/{courier_id}')

    @allure.title('Проверка статус-кода при попытке создать курьера с уже занятым логином')
    @allure.description('Происходит попытка создания нового курьера и проверяется статус-код')
    def test_same_login_status_code(self,courier):
        password = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"login": courier["login"], "password": password, "firstName": first_name}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409

    @allure.title('Проверка текста ошибки при попытке создать курьера с уже занятым логином')
    @allure.description('Происходит попытка создания нового курьера и проверяется текст ошибки')
    def test_same_login_error_message(self,courier):
        password = DataGenerate.generate_random_string(10)
        first_name = DataGenerate.generate_random_string(10)
        payload = {"login": courier["login"], "password": password, "firstName": first_name}
        response = requests.post(urls.URL_CREATE_COURIER, data=payload)
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."












