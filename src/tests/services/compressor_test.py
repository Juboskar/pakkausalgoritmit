import unittest
from unittest.mock import Mock
from services.compressor import Compressor


class TestCompressor(unittest.TestCase):
    def setUp(self):
        self.lz_mock = Mock()
        self.huff_mock = Mock()
        self.c = Compressor(self.lz_mock, self.huff_mock)

    def test_compressor_calls_lz_compress_when_lz_selected(self):
        self.c.compress_file("test_files/test_file.txt", "lz")
        self.lz_mock.compress.assert_called_with("Hello tests")

    def test_compressor_not_call_huff_compress_when_lz_selected(self):
        self.c.compress_file("test_files/test_file.txt", "lz")
        self.huff_mock.compress.assert_not_called()

    def test_compressor_calls_huff_compress_when_huff_selected(self):
        self.c.compress_file("test_files/test_file.txt", "huff")
        self.huff_mock.compress.assert_called_with("Hello tests")

    def test_compressor_not_call_lz_compress_when_huff_selected(self):
        self.c.decompress_file("test_files/test_file.txt", "huff")
        self.lz_mock.compress.assert_not_called()

    def test_compressor_calls_lz_decompress_when_lz_selected(self):
        self.c.decompress_file("test_files/test_file.txt", "lz")
        self.lz_mock.decompress.assert_called_with("Hello tests")

    def test_compressor_not_call_huff_decompress_when_lz_selected(self):
        self.c.decompress_file("test_files/test_file.txt", "lz")
        self.huff_mock.decompress.assert_not_called()

    def test_compressor_calls_huff_decompress_when_huff_selected(self):
        self.c.decompress_file("test_files/test_file.txt", "huff")
        self.huff_mock.decompress.assert_called_with("Hello tests")

    def test_compressor_not_call_lz_decompress_when_huff_selected(self):
        self.c.decompress_file("test_files/test_file.txt", "huff")
        self.lz_mock.decompress.assert_not_called()