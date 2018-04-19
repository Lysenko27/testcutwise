import pytest

from client.exception import ClientRuntimeException
from utils.exception_utils import check_exception
from utils.helper import generate_guid, get_random_text


@pytest.fixture(scope='module', autouse=True)
def pre_test_data(client):
	pass


def delete_list_correct_list_id(client):
	access_token = generate_guid()#принадлежит  выбранному SearchList access_token
	list_id =generate_guid()
	client.create_board(list_id,get_random_text(),access_token,get_random_text())
	public_list =client.delete_list(list_id,access_token)
	assert public_list['message']=='успешно удален'

def delete_list_not_correct_list_id(client):
	access_token = generate_guid()# не принадлежит  выбранному SearchList access_token
	with pytest.raises(ClientRuntimeException) as e:
		client.public_list(generate_guid(),access_token)
	assert check_exception(e, 'код ошибки', 'list_id не найден')

