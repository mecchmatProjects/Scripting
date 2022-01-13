import hashlib

arg = b'secret'
hasher = hashlib.blake2b(digest_size=10, salt=b'123')
hasher.update(arg)
print(hasher.hexdigest())
# output: 21ae7e05e9b6eceebfcf
hasher = hashlib.blake2b(digest_size=10, salt=b'abc')
hasher.update(arg)
print(hasher.hexdigest())
# output: 111c79c772defbed582e