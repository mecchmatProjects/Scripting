import secrets

data = '123abc!'
for i in range(5):
    print(secrets.choice(data), end=' ')
# output: c a 2 3 !