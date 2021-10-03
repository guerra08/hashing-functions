def read_file(file_name):
    f = open(file_name, "rb")
    file_bytes = []
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        file_bytes += [chunk]
    f.close()
    return file_bytes
