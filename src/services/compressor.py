"Tekstitiedostot merkkijonona algoritmeille siirtävä koodi"
from services.huffman import HuffmanCompressor, HuffmanDecompressor
from services.lempel_ziv import LzAlgorithm
from services.fileIO import FileIO


class Compressor:
    "Tekstitiedostot merkkijonona algoritmeille siirtävä luokka"

    def __init__(self, lempel_ziv=LzAlgorithm(), huff=HuffmanCompressor(),
                 huff_decompressor=HuffmanDecompressor(), file_io=FileIO()):
        self.lempel_ziv = lempel_ziv
        self.huff = huff
        self.huff_decompressor = huff_decompressor
        self.filename = None
        self.file_io = file_io

    def compress_file(self, uncompressed, selected_algorithm):
        """Avaa tiedoston ja antaa sisällön merkkijonona valitulla algoritmilla
        (lz/huff) pakkaavalle luokalle"""
        self.filename = uncompressed
        data = self.file_io.read(self.filename, "r", encoding="utf-8")

        if selected_algorithm == "lz":
            self.lempel_ziv.compress(data)
        elif selected_algorithm == "huff":
            self.file_io.write_bin(self.filename, self.huff.compress(data))

    def decompress_file(self, compressed, selected_algorithm):
        self.filename = compressed
        """Avaa pakatun tiedoston ja antaa sisällön merkkijonona valitulla algoritmilla
        (lz/huff) purkavalle luokalle"""
        data = self.file_io.read(self.filename, "rb")
        if selected_algorithm == "lz":
            self.lempel_ziv.decompress(data)
        elif selected_algorithm == "huff":
            self.file_io.write(self.filename, self.huff_decompressor.decompress(data))

    def save_decompressed(self, string):
        with open(self.filename + "_decompressed.txt", "w", encoding="utf-8") as decompressed_file:
            decompressed_file.write(string)
