#using random alphabets
import random as rd
otp="".join([str(rd.choice('abcdefghijklmnopqrstuvwxyz')) for i in range(16)])
print(f"Your OTP:{otp}")

#using random characters
otp="".join([str(rd.choice('!@#$%^&*()_+')) for i in range(16)])
print(f"Your OTP:{otp}")

import string
import secrets

# Define the pool of characters
alphabet = string.ascii_letters + string.digits + string.punctuation

# Generate a secure 16-character password
password = ''.join(secrets.choice(alphabet) for _ in range(16))
print(f"Generated Password: {password}")
