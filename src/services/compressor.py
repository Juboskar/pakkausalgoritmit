from services.compress_algorithms import LzAlgorithm, HuffmanAlgorithm


class Compressor:
    def __init__(self, lz=LzAlgorithm(), huff=HuffmanAlgorithm()):
        self.lz = lz
        self.huff = huff

    def compress_file(self, file, selected_algorithm):
        """Avaa tiedoston ja antaa sisällön merkkijonona valitulla algoritmilla (lz/huff) pakkaavalle luokalle"""
        with open(file) as file:
            if selected_algorithm == "lz":
                self.lz.compress(file.read())
            elif selected_algorithm == "huff":
                self.huff.compress(file.read())

    def return_decompressed(self, packed_file):
        pass
