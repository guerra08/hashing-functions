from crypto.sha import hash_block

def process_file(file_bytes):
    file_bytes.reverse()
    first_block = file_bytes[0]
    print(hash_block(first_block))
    return
