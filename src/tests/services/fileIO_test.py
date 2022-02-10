import unittest
from services.file_io import FileIO


class TestCompressor(unittest.TestCase):
    def setUp(self):
        self.file_io = FileIO()

    def test_read_text_files(self):
        self.assertEqual(self.file_io.read("test_files/read_test_file.txt", "r", encoding="utf-8"), "Hello tests")

    def test_read_binary_files(self):
        self.assertEqual(self.file_io.read("test_files/read_test_file.bin", "rb"),
                         b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', "
                         b"'s': '11'}\x01\xa8\x98\xc2\xc6")

    def test_write_text_files(self):
        self.file_io.write("test_files/write_test_file.txt", "w", "Hello tests")
        self.assertEqual(self.file_io.read("test_files/write_test_file.txt", "r", encoding="utf-8"), "Hello tests")

    def test_write_bin_files(self):
        self.file_io.write("test_files/write_test_file.bin", "wb",
                           b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', "
                           b"'s': '11'}\x01\xa8\x98\xc2\xc6")
        self.assertEqual(self.file_io.read("test_files/write_test_file.bin", "rb"),
                         b"\x00\x00\x00S{'t': '000', 'l': '001', 'e': '010', ' ': '011', 'o': '100', 'H': '101', "
                         b"'s': '11'}\x01\xa8\x98\xc2\xc6")
