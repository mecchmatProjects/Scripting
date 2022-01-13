import hashlib

hasher = hashlib.sha256()
hasher.update(b'secret')
print(hasher.digest_size)
# output: 32