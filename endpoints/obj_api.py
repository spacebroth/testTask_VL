import allure
from utils.api import TestAPI


class ObjApi(TestAPI):
    @allure.step('Создание объекта (/create_object)')
    def create_obj(self, key, value):
        json_obj = {f'{key}': f'{value}'}
        return self._send_post('/create_object', json_obj)

    @allure.step('Получение объекта (/get_object/[object_id])')
    def get_obj(self, obj_id):
        return self._send_get(f'/get_object/{obj_id}')
