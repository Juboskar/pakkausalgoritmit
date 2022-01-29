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

    def decompress_file(self, packed_file, selected_algorithm):
        """Avaa pakatun tiedoston ja antaa sisällön merkkijonona valitulla algoritmilla (lz/huff) purkavalle luokalle"""
        with open(packed_file) as file:
            if selected_algorithm == "lz":
                self.lz.compress(file.read())
            elif selected_algorithm == "huff":
                self.huff.decompress(file.read())
