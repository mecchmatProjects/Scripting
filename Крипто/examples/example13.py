import secrets, string

password = ''
for i in range(10):
    password += secrets.choice(string.ascii_letters + string.digits)
print(password)
# output: aCu27tEEDn