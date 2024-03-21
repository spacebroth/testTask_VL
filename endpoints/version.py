import allure
from utils.api import TestAPI


class VersionApi(TestAPI):
    @allure.step('Получение версии ПО (/version)')
    def get_version(self):
        return self._send_get('/version')
