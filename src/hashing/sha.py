from hashlib import sha256

def hash_block(block):
    return sha256(block).hexdigest()
