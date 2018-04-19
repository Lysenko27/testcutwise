from client.client import Client


class ApiMethods(Client):
	def __init__(self, settings):
		super().__init__(settings)


	def create_board(self, search_list_uuid, title, access_token, description,mediaSize='medium'):
		body = {
			 "searchList": search_list_uuid,
			 "title": title,
			 "description": description,
			 "active": True,
			 "settings": {
			  "isSingleScale": True,
			  "isGrayscale": True,
			  "isHiddenDesc": True,
			  "setupPreset": 21,
			  "background": {
				      "url": "https://super.bg/img.jpg"
				  },
			  "mediaSize": mediaSize
			 }
			}
		return self._post_request('/api/v2/boards?access_token=%s'%access_token, body)

	def public_list(self, list_id, access_token):
		params = {
			'access_token':access_token
		}

		return self._get_request('/api/v2/boards/%s'%list_id, params)

	def delete_list(self,list_id, access_token):
		pass

	def user_subscription_manipulation(self, access_token):
		pass

