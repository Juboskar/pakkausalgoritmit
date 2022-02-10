class FileIO:
    def __init__(self):
        pass

    def read(self, *args, **kwargs):
        with open(*args, **kwargs) as rfile:
            return rfile.read()

    def write(self, filename, write_type, data):
        with open(filename, write_type) as decompressed:
            decompressed.write(data)
