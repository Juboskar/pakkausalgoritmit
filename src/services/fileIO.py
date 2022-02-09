class FileIO:
    def __init__(self):
        pass

    def read(self, *args, **kwargs):
        with open(*args, **kwargs) as rfile:
            return rfile.read()

    def write(self, filename, data):
        with open(filename + "_huffman_decompressed.txt", "w") as decompressed:
            decompressed.write(data)

    def write_bin(self, filename, data):
        with open(filename + "_huffman_compressed.bin", "wb") as compressed:
            compressed.write(data)
