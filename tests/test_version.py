import allure
from schemas.version_schema import GetVersionResponse


@allure.suite('Version')
class TestVersion:
    @allure.title('Получение версии, возвращает словарь с ключами "major" (int>0) и "minor" (int>0)')
    def test_get_object(self, asserts, client):
        ver_res = client.version().get_version()
        asserts.status_code(ver_res, 200)
        asserts.validate_res(ver_res, GetVersionResponse)
