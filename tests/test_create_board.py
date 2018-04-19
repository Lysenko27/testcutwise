import pytest

from client.exception import ClientRuntimeException
from utils.exception_utils import check_exception
from utils.helper import generate_guid, get_random_text


@pytest.fixture(scope='module', autouse=True)
def pre_test_data(client):
	pass


def greate_board_conflict(client):
	access_token = generate_guid()#принадлежит  выбранному SearchList access_token
	client.create_board(generate_guid(),get_random_text(),access_token,get_random_text())
	with pytest.raises(ClientRuntimeException) as e:
		client.create_board(generate_guid(),get_random_text(),access_token,get_random_text())
	assert check_exception(e, 409, 'Conflict')

def greate_board_do_not_belong_access_token(client):
	access_token = generate_guid()# не принадлежит  выбранному SearchList access_token
	with pytest.raises(ClientRuntimeException) as e:
		client.create_board(generate_guid(),get_random_text(),access_token,get_random_text())
	assert check_exception(e, 'код ошибки', 'текст')

def greate_board(client):
	access_token = generate_guid()#принадлежит  выбранному SearchList access_token
	client.create_board(generate_guid(),get_random_text(),access_token,get_random_text(),'small')
	access_token = generate_guid()#принадлежит  выбранному SearchList access_token
	client.create_board(generate_guid(),get_random_text(),access_token,get_random_text(),'large')
	with pytest.raises(ClientRuntimeException) as e:
		client.create_board(generate_guid(),get_random_text(),access_token,get_random_text(),'round')
	assert check_exception(e, 'код ошибки', 'текст')