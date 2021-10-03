from crypto.sha import hash_block

def process_file(file_bytes):
    file_bytes.reverse()
    last_hash = ""
    while len(file_bytes) > 0:
        block = file_bytes.pop(0)
        block += bytearray.fromhex(last_hash)
        last_hash = hash_block(block)
    return last_hash
