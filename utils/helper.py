import random
import string
import uuid

def generate_guid():
	return str(uuid.uuid4())

def get_random_text(n=50, m=100):
	return ''.join([random.choice(string.ascii_letters) for i in range(random.randint(n, m))])
