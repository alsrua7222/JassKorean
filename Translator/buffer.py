def read_stream(filename, size=1024):
    buffer = bytearray()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(size)
            
            if not data:
                break

            buffer.extend(data)
            
            if buffer:
                yield buffer.decode()
    return