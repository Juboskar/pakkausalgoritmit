import unittest
from services.huffman import HuffmanCompressor, HuffmanDecompressor


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.huffman = HuffmanCompressor()
        self.huffman_decompressor = HuffmanDecompressor()

    def test_tree_is_correct(self):
        self.huffman.build_tree("AAAAABCCCDD")
        self.assertEqual(str(self.huffman.tree),
                         "Node: None: 11, (Node: A: 5, (None, None), " +
                         "Node: None: 6, (Node: C: 3, (None, None), " +
                         "Node: None: 3, (Node: B: 1, (None, None), " +
                         "Node: D: 2, (None, None))))")

    def test_bit_values_are_calculated_correctly(self):
        self.huffman.build_tree("AAAAABCCCDD")
        self.assertEqual(self.huffman.calculate_bit_values(),
                         {'D': '000', 'B': '001', 'C': '01', 'A': '1'})

    def test_compress(self):
        self.assertEqual(self.huffman.compress("AAAAABCCCDD"),
                         b"\x00\x00\x00-{'D': '000', 'B': '001', 'C': '01', 'A': '1'}\x04\xf9T\x00")

    def test_decompress(self):
        self.assertEqual(self.huffman_decompressor.decompress(
            b"\x00\x00\x00-{'D': '000', 'B': '001', 'C': '01', 'A': '1'}\x04\xf9T\x00"), "AAAAABCCCDD")
