import secrets, string

password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
print(password)
# output: WRC3gb6RX1