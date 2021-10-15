from hashlib import sha256

def hash_block(block):
    """Performs a SHA265 hashing on bytes
    
    Parameters:
        block: Bytes to be hashed

    Returns
        string: Hash result

    """
    return sha256(block).hexdigest()
