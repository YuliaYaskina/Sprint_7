from conftest import courier
import requests
import urls
from helpers.data_generator import DataGenerate
import allure

class TestCourierLogin:
    @allure.title('Проверка логина курьера')
    @allure.description('Отправляются валидные значения логиина и пароля и проверяется успешный логин')
    def test_courier_auth(self, courier):
        payload = {"login": courier["login"], "password": courier["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.status_code == 200

    @allure.title('Проверка статус-кода, если не передается логин')
    @allure.description('Отправляется запрос с пустым значением логина и проверяется статус-код')
    def test_no_login_status_code(self,courier):
        payload = {"login": "", "password": courier["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка текста ошибки, если не передается логин')
    @allure.description('Отправляется запрос с пустым значением логина и проверяется текст ошибки')
    def test_no_login_error_text(self,courier):
        payload = {"login": "", "password": courier["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка статус-кода, если не передается пароль')
    @allure.description('Отправляется запрос с пустым значением пароля и проверяется статус-код')
    def test_no_password_status_code(self,courier):
        payload = {"login": courier["login"], "password": ""}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка текста ошибки, если не передается пароль')
    @allure.description('Отправляется запрос с пустым значением пароля и проверяется текст ошибки')
    def test_no_password_error_text(self,courier):
        payload = {"login": courier["login"], "password": ""}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка статус-кода, если передается несуществующий логин')
    @allure.description('Отправляется запрос с рандомным логином и проверяется статус код')
    def test_courier_incorrect_login_status_code(self,courier):
        login = DataGenerate.generate_random_string(10)
        payload = {"login": login, "password": courier["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.status_code == 404

    @allure.title('Проверка текста ошибки, если передается несуществующий логин')
    @allure.description('Отправляется запрос с рандомным логином и проверяется текст ошибки')
    def test_courier_incorrect_login_error_message(self,courier):
        login = DataGenerate.generate_random_string(10)
        payload = {"login": login, "password": courier["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка статус-кода, если передается некорректный пароль')
    @allure.description('Отправляется запрос с рандомным паролем и проверяется статус-код')
    def test_courier_incorrect_password_status_code(self,courier):
        password = DataGenerate.generate_random_string(10)
        payload = {"login": courier["login"], "password": password}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.status_code == 404

    @allure.title('Проверка текста ошибки, если передается некорректный пароль')
    @allure.description('Отправляется запрос с рандомным паролем и проверяется текст ошибки')
    def test_courier_incorrect_password_error_message(self,courier):
        password = DataGenerate.generate_random_string(10)
        payload = {"login": courier["login"], "password": password}
        response = requests.post(urls.URL_LOGIN, data=payload)
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка возвращения id курьера при успешном логине')
    @allure.description('Отправляются валидные значения логина и пароля и проверяется получение id')
    def test_courier_return_id(self,courier):
        payload = {"login": courier["login"], "password": courier["password"]}
        response = requests.post(urls.URL_LOGIN, data=payload)
        try:
            response.json()['id']
        except KeyError:
            raise AssertionError("Не найдено поле 'id'")

















