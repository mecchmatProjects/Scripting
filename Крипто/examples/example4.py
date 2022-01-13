import hashlib

hasher = hashlib.sha256()
hasher.update(b'secret')
print(hasher.digest())
# output: b"+\xb8\rS{\x1d\xa3\xe3\x8b\xd3\x03a\xaa\x85V\x86\xbd\xe0\xea\xcdqb\xfe\xf6\xa2_\xe9{\xf5'\xa2["

