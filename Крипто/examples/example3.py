import hashlib

hasher = hashlib.sha256()
hasher.update('secret'.encode(encoding='ascii'))
print(hasher.hexdigest())
# output: 2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b