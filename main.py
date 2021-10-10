import string
import random

chars = list(string.ascii_letters + "!@#$%^&*()" + string.digits)
def generate_random_password():
	l = int(9)
	random.shuffle(chars)
	password = []
	for i in range(l):
  	  password.append(random.choice(chars))
	random.shuffle(password)
	print("".join(password))
generate_random_password()