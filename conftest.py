import pytest
from endpoints.common_validators import Asserts
from utils.api import TestAPI

BASE_URL = 'https://api.example.tech'


@pytest.fixture(scope='session')
def asserts():
    return Asserts()


@pytest.fixture(scope='class')
def client():
    return TestAPI(BASE_URL)


@pytest.fixture
def obj():
    response = TestAPI(BASE_URL).object().create_obj('a', 'TEST!@#$%^&*()_+qwerty')
    return response


# Некоторые тесты могут быть зависимы от версии или на некоторых версиях тест не актуален. Перед запуском тестов
# можно узнать её, а затем использовать IF в тестах.
# К примеру использовать @pytest.mark.skipif(check_version < 2.0, reason='Тест не актуален для версии меньше 2.0')
@pytest.fixture(scope='session')
def check_version():
    res = TestAPI(BASE_URL).version().get_version()
    version = float(f'{res["major"]}.{res["minor"]}')
    return version
