import hashlib

arg = b'secret'
hasher = hashlib.blake2b(digest_size=10)
hasher.update(arg)
print(hasher.hexdigest())
# output: 9bbfac49bef7ad7d0b64
hasher = hashlib.blake2b(digest_size=15)
hasher.update(arg)
print(hasher.hexdigest())
# output: 36dac4d6731cbe172d9e2e03af80a0