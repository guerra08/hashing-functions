from crypto.sha import hash_block
from utils.iter import group

def process_file(file_bytes):
    grouped = group(file_bytes, 1024)
    grouped.reverse()
    first_block = grouped[0]
    block_bytes = ""
    for byte in first_block:
        block_bytes += str(byte)
    print(block_bytes)
    return
