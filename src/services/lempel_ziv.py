"""Lempel-Ziv Algorithm"""
from services.utilities import list_bytes_to_list


class LzCompressor:
    """Lempel-Ziv compressing-algorithm"""

    def __init__(self):
        self.output_byte_array = b''
        self.string_list = []
        self.string = ''

    def encode_string(self):
        """Calculates output int values from string"""
        output = []
        previous_char = ''
        for char in self.string:
            if previous_char + char in self.string_list:
                previous_char += char
            else:
                output.append(self.string_list.index(previous_char))
                self.string_list.append(previous_char + char)
                previous_char = char
        output.append(self.string_list.index(previous_char))
        return output

    def compress(self, string: str):
        """Compresses with Lempel-Ziv algorithm"""
        initial = sorted(list(set(string)))  # sorted testejä varten
        self.string_list = initial.copy()
        self.string = string
        encoded_values = bytearray(str(initial).encode('ascii'))
        header = len(encoded_values).to_bytes(4, 'big')

        self.output_byte_array = header + bytearray(str(initial).encode('ascii'))
        for i in [i.to_bytes(2, byteorder='big') for i in self.encode_string()]:
            self.output_byte_array += i
        return self.output_byte_array


class LzDecompressor:
    """Lempel-Ziv decompressing-algorithm"""

    def __init__(self):
        self.bytes_array = b''
        self.values_length = 0
        self.values = []
        self.bytes_int_values = []

    def bytes_to_int(self):
        """Returns encoded int values from bytearray"""
        bytes_int_values = []
        i = self.values_length + 4
        while i < len(self.bytes_array):
            bytes_int_values.append(int.from_bytes(self.bytes_array[i:i + 2], 'big'))
            i += 2
        return bytes_int_values

    def decode_values(self):
        """Decodes int values and returns decoded string"""
        value = self.values[self.bytes_int_values.pop(0)]
        output = value
        for i in self.bytes_int_values:
            if i < len(self.values):
                decoded = self.values[i]
            else:
                decoded = value + value[0]
            output += decoded
            self.values.append(value + decoded[0])
            value = decoded
        return output

    def decompress(self, bytes_array: str):
        """Decompresses lempel-ziv packed bytearray"""
        self.bytes_array = bytes_array
        self.values_length = int.from_bytes(self.bytes_array[0:4], 'big')
        self.values = list_bytes_to_list(self.bytes_array[4:self.values_length + 4])

        self.bytes_int_values = self.bytes_to_int()
        output = self.decode_values()

        return output
