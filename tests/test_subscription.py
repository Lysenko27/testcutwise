import pytest
from utils.helper import generate_guid


@pytest.fixture(scope='module', autouse=True)
def pre_test_data(client):
	pass


def user_subscription_manipulation_s1(client):
	access_token = generate_guid()#у которого запрос отправлен,но ещё не реагировал
	subscription=client.user_subscription_manipulation(access_token)
	assert subscription['status']=='1'

def user_subscription_manipulation_s2(client):
	access_token = generate_guid()#реагировал, но не подписан на public list
	subscription=client.user_subscription_manipulation(access_token)
	assert subscription['status']=='2'

def user_subscription_manipulation_s3(client):
	access_token = generate_guid()#подписан
	subscription =client.user_subscription_manipulation(access_token)
	assert subscription['status']=='3'