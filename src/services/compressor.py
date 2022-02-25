"""Code for giving text file contents to compressing and decompressing algorithms"""
from services.huffman import HuffmanCompressor, HuffmanDecompressor
from services.lempel_ziv import LzCompressor, LzDecompressor
from services.file_io import FileIO


class Compressor:
    """Gives text file contents to compressing and decompressing algorithms"""

    def __init__(self, lz=LzCompressor(), lz_decompressor=LzDecompressor(),  # pylint: disable=R0913
                 huff=HuffmanCompressor(), huff_decompressor=HuffmanDecompressor(),
                 file_io=FileIO()):
        self.lz = lz
        self.lz_decompressor = lz_decompressor
        self.huff = huff
        self.huff_decompressor = huff_decompressor
        self.filename = None
        self.file_io = file_io

    def compress_file(self, uncompressed, selected_algorithm):
        """Opens file and saves compressed content"""
        self.filename = uncompressed
        data = self.file_io.read(self.filename, "r", encoding="utf-8")

        if selected_algorithm == "lz":
            self.file_io.write(self.filename + "_lz_compressed.bin", "wb",
                               self.lz.compress(data))
        elif selected_algorithm == "huff":
            self.file_io.write(self.filename + "_huffman_compressed.bin", "wb",
                               self.huff.compress(data))

    def decompress_file(self, compressed, selected_algorithm):
        """Opens file and saves decompressed content"""
        self.filename = compressed
        data = self.file_io.read(self.filename, "rb")
        if selected_algorithm == "lz":
            self.file_io.write(self.filename + "_lz_decompressed.txt", "w",
                               self.lz_decompressor.decompress(data))
        elif selected_algorithm == "huff":
            self.file_io.write(self.filename + "_huffman_decompressed.txt", "w",
                               self.huff_decompressor.decompress(data))
