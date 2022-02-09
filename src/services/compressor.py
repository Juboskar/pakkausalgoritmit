"Tekstitiedostot merkkijonona algoritmeille siirtävä koodi"
from services.huffman import HuffmanCompressor, HuffmanDecompressor
from services.lempel_ziv import LzAlgorithm


class Compressor:
    "Tekstitiedostot merkkijonona algoritmeille siirtävä luokka"

    def __init__(self, lempel_ziv=LzAlgorithm(), huff=HuffmanCompressor(), huff_decompressor=HuffmanDecompressor()):
        self.lempel_ziv = lempel_ziv
        self.huff = huff
        self.huff_decompressor = huff_decompressor
        self.filename = None

    def compress_file(self, uncompressed, selected_algorithm):
        """Avaa tiedoston ja antaa sisällön merkkijonona valitulla algoritmilla
        (lz/huff) pakkaavalle luokalle"""
        self.filename = uncompressed
        with open(self.filename, "r", encoding="utf-8") as uncompressed_file:
            if selected_algorithm == "lz":
                self.lempel_ziv.compress(uncompressed_file.read())
            elif selected_algorithm == "huff":
                self.save(self.huff.compress(uncompressed_file.read()))

    def save(self, bytes):
        """Tallentaa binääritiedostona pakatut"""
        with open(self.filename + ".bin", "wb") as compressed:
            compressed.write(bytes)

    def decompress_file(self, compressed, selected_algorithm):
        self.filename = compressed
        """Avaa pakatun tiedoston ja antaa sisällön merkkijonona valitulla algoritmilla
        (lz/huff) purkavalle luokalle"""
        with open(compressed, "rb") as compressed_file:
            if selected_algorithm == "lz":
                self.lempel_ziv.decompress(compressed_file.read())
            elif selected_algorithm == "huff":
                self.save_decompressed(self.huff_decompressor.decompress(compressed_file.read()))

    def save_decompressed(self, string):
        with open(self.filename + "_decompressed.txt", "w", encoding="utf-8") as decompressed_file:
            decompressed_file.write(string)
