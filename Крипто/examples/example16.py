import secrets

print(secrets.token_bytes(10))
# output: b'\x0c\x14\x9a\xad\x1f\x06\xb8\x9d~'
print(secrets.token_hex(10))
# output: 73ece06e05057f952315
print(secrets.token_urlsafe(10))
# output: NXG4GdcQ3AEzdw