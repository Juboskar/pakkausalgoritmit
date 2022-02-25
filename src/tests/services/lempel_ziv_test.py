import unittest
from services.lempel_ziv import LzCompressor, LzDecompressor


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.lz = LzCompressor()
        self.lz_decompressor = LzDecompressor()

    def test_compress(self):
        self.assertEqual(self.lz.compress("AAAAABCCCDD"),
            b"\x00\x00\x00\x14['A', 'B', 'C', 'D']\x00\x00\x00\x04\x00\x04\x00\x01\x00\x02\x00\x08\x00\x03\x00\x03")

    def test_decompress(self):
        self.assertEqual(self.lz_decompressor.decompress(
            b"\x00\x00\x00\x14['A', 'B', 'C', 'D']\x00\x00\x00\x04\x00\x04\x00\x01\x00\x02\x00\x08\x00\x03\x00\x03"),
            "AAAAABCCCDD")
