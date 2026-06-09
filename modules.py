from math import sqrt,ceil,floor
print(sqrt(5))
print(ceil(5.2))
print(floor(5.8))

#From
import random as rd
print(rd.randint(1,10))

#rd integers
print(rd.randint(1,10))
print(rd.randrange(0,10,2))

#rd float
print(rd.rd())
print(rd.uniform(1.5,10.5))

#choosing from sequence
colours=['red','green','blue','yellow']
print(rd.choice(colours))
print(rd.choices(colours,k=2))

#seed
import random as rd
rd.seed(42)
print(rd.randint(1,100))
print(rd.randint (1,100))

#OTP Generator
otp="".join([str(rd.randint(0,9)) for i in range(6)])
print(f"Your OTP:{otp}")

#for security purpose we can use secrets module
import secrets
secure_token=secrets.token_hex(16)
print(f"Your secure token: {secure_token}")