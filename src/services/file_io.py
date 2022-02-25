"""Reads and writes files"""


class FileIO:
    """Reads and writes files"""

    def __init__(self):
        pass

    @staticmethod
    def read(*args, **kwargs):
        """Gets file name, type and encoding and returns file content"""
        with open(*args, **kwargs) as rfile:  # pylint: disable=W1514
            return rfile.read()

    @staticmethod
    def write(filename, write_type, data):
        """Gets file name, type and adta and writes content to file"""
        with open(filename, write_type) as decompressed:  # pylint: disable=W1514
            decompressed.write(data)
