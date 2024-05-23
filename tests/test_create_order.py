import pytest
import requests
import urls
import json
import allure

class TestOrderCreation:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверяется создание заказа с разными значениями поля "color"')
    @pytest.mark.parametrize('color',
                             [["BLACK"],
                              ["GREY"],
                              [],
                              ['BLACK', 'GREY']]
                             )
    def test_order_creation(self, color):
        payload = {'firstName': 'Имя', 'lastName': 'Фамилия', 'address': 'Адрес',
                   'metroStation': 'Станция Метро', 'phone': '+70000000000',
                   'rentTime': 100, 'deliveryDate': '01/01/2001', 'comment': 'комментарий', 'color': color}
        response = requests.post(urls.URL_CREATE_ORDER, data=json.dumps(payload), headers={"Content_Type":"application/json"})
        assert 'track' in response.json()




