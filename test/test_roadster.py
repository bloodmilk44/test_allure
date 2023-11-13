import allure
import requests as api

roadster_url = 'https://api.spacexdata.com/v3/roadster'


@allure.title('main test')
def test_1():
    test = api.get(roadster_url)
    body = test.json()
    with allure.step('check title'):
        assert body['name'] == "Elon Musk's Tesla Roadster"
    with allure.step('check status code'):
        assert test.status_code == 200
