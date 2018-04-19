from http.client import HTTPResponse
from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPCookieProcessor, Request

from json import loads, dumps
from typing import Dict

from client.exception import ClientServerException, ClientRuntimeException


class Client(object):
	def __init__(self, settings):
		self.api = settings['server']

		self.opener = build_opener(HTTPCookieProcessor(CookieJar()))

		login_data = urlencode({'username': settings['username'], 'password': settings['password']}).encode()
		self.opener.open(Request(settings['server'] + '/login', login_data))


	def _post_request(self, url: str, data, params={}):
		request_data = dumps(data, default=lambda o: o.__dict__).encode()

		params_url = '&'.join('{}={}'.format(key, value) for key, value in params.items() if value is not None)

		request = Request(self.api + url + '?' + params_url, request_data,
		                  {'Content-Type': 'application/json', 'Accept': 'application/json'})
		return self.__processing_response(self.opener.open(request))

	def _get_request(self, url: str, params: Dict[str, object]):
		params_url = '&'.join('{}={}'.format(key, value) for key, value in params.items() if value is not None)
		request = Request(self.api + url + '?' + params_url, headers={'Accept': 'application/json'})
		return self.__processing_response(self.opener.open(request))

	@staticmethod
	def __processing_response(response: HTTPResponse):
		if response.code == 200:
			data = loads(response.read().decode())
			if data['status'] == 0:
				return data['data'] if 'data' in data else data
			else:
				if 'validationErrors' in data:
					raise ClientRuntimeException(data['status'], 'Ошибка запроса: {message}'.format(
						message=data['message'] + '' + '!' + data['validationErrors'][0]['description'] + '' +
						        data['validationErrors'][0]['field']))
				else:
					raise ClientRuntimeException(data['status'],
					                         'Ошибка запроса: {message}'.format(message=data['message']))
		else:
			raise ClientServerException('Ошибка обращения к серверу: {code}'.format(code=response.code))
