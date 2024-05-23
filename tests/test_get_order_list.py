import requests
import urls
from conftest import courier_auth
import allure

class TestGetOrderList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Отправляется запрос на получение списка заказов, проверяется, что список заказов не пустой')
    def test_order_list(self, courier_auth):
        response = requests.get(urls.URL_GET_ORDER_LIST)
        assert len(response.json()['orders']) != 0