import secrets, string

while True:
    password = ''.join(secrets.choice(string.ascii_letters + 
        string.digits + string.punctuation) for i in range(10))
    if (sum(c.isdigit() for c in password) >= 2 and 
        any(c.isupper() for c in password) and 
        any(c in string.punctuation for c in password)):
        break
print(password)
# output: 5Dz/>!"3Qp