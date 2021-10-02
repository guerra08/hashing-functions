def read_file(file_name):
    with open(file_name, "rb") as f:
        blist = list(bytearray(f.read()))
        return blist
