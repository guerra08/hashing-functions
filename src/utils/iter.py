def group(iterable, n):
    chunks = []
    for i in range(0, len(iterable), n):
        chunks += [iterable[i:i+n]]
    return chunks
