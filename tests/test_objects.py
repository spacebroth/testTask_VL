import allure
import pytest
from schemas.objects.create_obj_scheme import CreateObjResponse, CreateObjErrorResponse
from schemas.objects.get_obj_scheme import GetObjResponse


@allure.suite('Objects')
class TestObjects:
    @allure.title('При создании объекта возвращается его ID, при ошибке - error')
    # @pytest.mark.objects
    @pytest.mark.parametrize('key, value, code', [('', 'a', 400),
                                                  ('a', '', 201),
                                                  ('a', 'a', 201),
                                                  (1, 'a', 400),
                                                  ('a', 1, 400),
                                                  (' ', 'QWE', 400),
                                                  ('a', ' ', 201),
                                                  (None, '$!@^&*', 400),
                                                  ('a', None, 201),
                                                  ('a', f'{"s" * 63}', 201),
                                                  ('a', f'{"s" * 64}', 201),
                                                  ('a', f'{"s" * 65}', 400)])
    def test_create_object(self, asserts, client, key, value, code):
        obj_res = client.object().create_obj(key, value)
        asserts.status_code(obj_res, code)
        if obj_res.status_code >= 400:
            asserts.validate_res(obj_res, CreateObjErrorResponse)
        else:
            asserts.validate_res(obj_res, CreateObjResponse)

    @allure.title('Получение объекта, возвращает объект по его ID')
    # @pytest.mark.objects
    def test_get_object(self, asserts, client, obj):
        obj_res = client.object().get_obj(obj.json()['id'])
        asserts.status_code(obj_res, 200)
        asserts.validate_res(obj_res, GetObjResponse)
        asserts.field_equals(obj_res.json()['id'] == obj['id'])  # Это если в ответе приходит ID
        asserts.field_equals(obj_res.json()['a'] == obj['a'])
