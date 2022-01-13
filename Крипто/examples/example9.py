import hashlib, hmac

key = b'key123' # private data
arg = b'secret' # public data
hasher = hmac.new(key=key, digestmod=hashlib.sha256)
hasher.update(arg)
print(hasher.hexdigest())
# output: c6b901d1f7bda154c6673a403c8e7b861db0fec293f36ed47ff4c50405e7d439
attackerHasher = hashlib.sha256()
attackerHasher.update(arg)
print(attackerHasher.hexdigest())
# output: 2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b