import os
from crypto.sha import hash_block

CHUNK_SIZE = 1024

def process_file(file_name):
    """Processes a file in blocks of 1024 bytes at a time and returns the H0 hash.

    Parameters:
        file_name: Name / path of the file

    Returns
        string: H0 hash
    """
    file_size = os.path.getsize(file_name)
    current_chunk_size = file_size % CHUNK_SIZE
    with open(file_name, "rb") as file:
        file.seek(0, os.SEEK_END)
        pointer_loc = file.tell()
        last_hash = ""
        while pointer_loc >= 0:
            file.seek(pointer_loc)
            pointer_loc = pointer_loc - current_chunk_size
            current_bytes = file.read(current_chunk_size)
            if current_chunk_size != CHUNK_SIZE:
                current_chunk_size = CHUNK_SIZE
            if len(current_bytes) > 0:
                current_bytes += bytearray.fromhex(last_hash)
                last_hash = hash_block(current_bytes)
        return last_hash
