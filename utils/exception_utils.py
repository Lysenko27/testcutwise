def check_exception(exception, status, message):
	return exception.value.status == status and exception.value.message == message
