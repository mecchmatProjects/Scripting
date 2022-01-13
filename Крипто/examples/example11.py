import secrets

result = secrets.randbits(10)
print(result)
# output: 994
print(bin(result))
# output: 0b1111100010