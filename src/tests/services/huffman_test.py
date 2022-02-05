import unittest
from services.huffman import HuffmanAlgorithm


class TestHuffman(unittest.TestCase):
    def test_tree_is_correct(self):
        huffman = HuffmanAlgorithm()
        huffman.build_tree("AAAAABCCCDD")
        self.assertEqual(str(huffman.tree),
                         "Node: None: 11, (Node: A: 5, (None, None), " +
                         "Node: None: 6, (Node: C: 3, (None, None), " +
                         "Node: None: 3, (Node: B: 1, (None, None), " +
                         "Node: D: 2, (None, None))))")

    def test_bit_values_are_calculated_correctly(self):
        huffman = HuffmanAlgorithm()
        huffman.build_tree("AAAAABCCCDD")
        self.assertEqual(huffman.bit_values(),
                         {'D': '000', 'B': '001', 'C': '01', 'A': '1'})
