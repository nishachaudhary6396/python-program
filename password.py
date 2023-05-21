import secrets
import string
alphabet = string.ascii_letters + string.digits + string.punctuation
password_length = 12
password = ''.join(secrets.choice(alphabet) for i in range(password_length))
print("Password generated:", password)
