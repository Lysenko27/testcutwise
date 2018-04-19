class ClientServerException(Exception):
	pass


class ClientRuntimeException(Exception):
	def __init__(self, status, message):
		super().__init__(message)
		self.status = status
		self.message = message
