import unittest
from unittest.mock import Mock
from services.compressor import Compressor


class FakeFileIO:
    def __init__(self):
        pass

    def read(self, filename, filetype, **kwargs):
        if filetype == "rb":
            return b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', 's': '11'}\x01\xa8\x98\xc2\xc6"
        elif filetype == "r":
            return "Hello tests"

    def write(self, filename, filetype, data):
        return


class TestCompressor(unittest.TestCase):
    def setUp(self):
        self.lz_mock = Mock()
        self.huff_mock = Mock()
        self.huff_mock.compress.return_value = \
            b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', 's': '11'}\x01\xa8\x98\xc2\xc6"
        self.huff_decompressor_mock = Mock()
        self.huff_decompressor_mock.decompress.return_value = "Hello tests"
        self.compressor = Compressor(self.lz_mock, self.huff_mock, self.huff_decompressor_mock, FakeFileIO())

    def test_compressor_calls_lz_compress_when_lz_selected(self):
        self.compressor.compress_file("hello.txt", "lz")
        self.lz_mock.compress.assert_called_with("Hello tests")

    def test_compressor_not_call_huff_compress_when_lz_selected(self):
        self.compressor.compress_file("hello.txt", "lz")
        self.huff_mock.compress.assert_not_called()

    def test_compressor_calls_huff_compress_when_huff_selected(self):
        self.compressor.compress_file("hello.txt", "huff")
        self.huff_mock.compress.assert_called_with("Hello tests")

    def test_compressor_not_call_lz_compress_when_huff_selected(self):
        self.compressor.decompress_file("hello.txt", "huff")
        self.lz_mock.compress.assert_not_called()

    def test_compressor_calls_lz_decompress_when_lz_selected(self):
        self.compressor.decompress_file("hello.bin", "lz")
        self.lz_mock.decompress.assert_called_with(
            b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', 's': '11'}\x01\xa8\x98\xc2\xc6")

    def test_compressor_not_call_huff_decompress_when_lz_selected(self):
        self.compressor.decompress_file("hello.bin", "lz")
        self.huff_decompressor_mock.decompress.assert_not_called()

    def test_compressor_calls_huff_decompress_when_huff_selected(self):
        self.compressor.decompress_file("hello.bin", "huff")
        self.huff_decompressor_mock.decompress.assert_called_with(
            b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', 's': '11'}\x01\xa8\x98\xc2\xc6")

    def test_compressor_not_call_lz_decompress_when_huff_selected(self):
        self.compressor.decompress_file("hello.bin", "huff")
        self.lz_mock.decompress.assert_not_called()
