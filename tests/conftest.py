import pytest

from client.api_methods import ApiMethods
from tests.settings import host


@pytest.fixture(scope='session')
def client():
	return ApiMethods(host())