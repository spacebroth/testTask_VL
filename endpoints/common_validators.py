from typing import Type
import allure
from re import sub, MULTILINE
from pydantic import ValidationError, BaseModel


class Asserts:
    @staticmethod
    @allure.step('Валидация полей и структуры ответа')
    def validate_res(response, model: Type[BaseModel]):
        """
        Проверяет тело ответа на соответствие его схеме JSON механизмами pydantic
        :param response: ответ от сервера
        :param model: модель, по которой будет проверяться схема JSON
        :raises AssertionError: если тело ответа не соответствует схеме
        """
        try:
            model.model_validate(response.json())
        except ValidationError as e:
            err = sub(r'For further information visit.*', '', str(e), flags=MULTILINE)
            raise AssertionError(err)

    @staticmethod
    @allure.step('Проверка, что ответ пришел с кодом {status_code}')
    def status_code(response, status_code: int):
        assert response.status_code == status_code

    @staticmethod
    @allure.step('Сравнение ожидаемого значения в поле с актуальным')
    def field_equals(response_field, expected_field):
        assert response_field == expected_field, (f'Актуальное и ожидаемое значения полей НЕ совпадают\n'
                                                  f'Актуальное: "{response_field}"\nОжидаемое: "{expected_field}"')
