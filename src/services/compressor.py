"Tekstitiedostot merkkijonona algoritmeille siirtävä koodi"
from services.huffman import HuffmanCompressor, HuffmanDecompressor
from services.lempel_ziv import LzAlgorithm
from services.file_io import FileIO


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
        """Avaa tiedoston ja pakkaa sisällön binääritiedostoon"""
        self.filename = uncompressed
        data = self.file_io.read(self.filename, "r", encoding="utf-8")

        if selected_algorithm == "lz":
            self.file_io.write(self.filename + "_lz_compressed.bin", "wb",
                               self.lempel_ziv.compress(data))
        elif selected_algorithm == "huff":
            self.file_io.write(self.filename + "_huffman_compressed.bin", "wb",
                               self.huff.compress(data))

    def decompress_file(self, compressed, selected_algorithm):
        """Avaa binääritiedoston ja purkaa sisällön tekstitiedostoon"""
        self.filename = compressed
        data = self.file_io.read(self.filename, "rb")
        if selected_algorithm == "lz":
            self.file_io.write(self.filename + "_lz_decompressed.txt", "w",
                               self.lempel_ziv.decompress(data))
        elif selected_algorithm == "huff":
            self.file_io.write(self.filename + "_huffman_decompressed.txt", "w",
                               self.huff_decompressor.decompress(data))
