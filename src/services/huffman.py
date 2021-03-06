"Huffman algorithm"
from services.utilities import list_bytes_to_list


class Node:
    """Node for Huffman-tree"""

    def __init__(self, symbol, value, left, right):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, comparable):
        """Method for finding node with smallest value"""
        return self.value < comparable.value

    def __str__(self):
        """String representation for debugging"""
        return f"Node: {self.symbol}: {self.value}, ({self.left}, {self.right})"


class HuffmanCompressor:
    """Class for Huffman compression"""

    def __init__(self):
        self.tree = None

    def build_tree(self, string: str):
        """Builds Huffman tree"""
        count = {}
        for i in string:
            count[i] = 1 if i not in count else count[i] + 1
        trees = [Node(symbol, value, None, None) for symbol, value in count.items()]
        while len(trees) > 1:
            min_node_1 = trees.pop(trees.index(min(trees)))
            min_node_2 = trees.pop(trees.index(min(trees)))
            trees.append(Node(None, min_node_1.value + min_node_2.value, min_node_1, min_node_2))
        self.tree = trees[0]

    def calculate_bit_values(self):
        """Returns decoding values as dictionary from Huffman tree"""
        bit_values = {}
        bits = ""
        node = self.tree

        def recursively_check_codes(tree_node, bit_string):
            if tree_node.symbol is not None:
                bit_values[tree_node.symbol] = bit_string
            else:
                recursively_check_codes(tree_node.right, bit_string + "0")
                recursively_check_codes(tree_node.left, bit_string + "1")

        recursively_check_codes(node, bits)
        return bit_values

    def compress(self, string: str):
        """Algorithm for Huffman compressing"""
        self.build_tree(string)
        values = self.calculate_bit_values()

        binary = ''.join([values[i] for i in string])
        n = len(binary)
        off = 0 if 8 - (n % 8) == 8 else 8 - (n % 8)
        binary += off * '0'
        integer_values = [off]
        for i in range(0, n, 8):
            integer_values.append(int(binary[i:i + 8], 2))

        encoded_values = bytearray(str(values).encode('ascii'))
        header = len(encoded_values).to_bytes(4, 'big')
        return header + bytearray(str(values).encode('ascii')) + bytearray(integer_values)


class HuffmanDecompressor:
    """Class for Huffman decompressing"""

    def __init__(self):
        self.values_length = None
        self.bytes_int_values = []

    def bytes_int_values_to_binary(self):
        """returns bytes values as binary string"""
        return "".join(map(lambda x: "{0:b}".format(x).zfill(8),  # pylint: disable=C0209
                           self.bytes_int_values[self.values_length + 5:]))

    def decompress(self, bytes_array: bytearray):
        """Algorithm for Huffman decompressing"""
        self.values_length = int.from_bytes(bytes_array[0:4], 'big')
        values = list_bytes_to_list(bytes_array[4:self.values_length + 4])

        self.bytes_int_values = list(bytes_array)

        off = self.bytes_int_values[self.values_length + 4]
        binary = self.bytes_int_values_to_binary()

        binary_string = binary if off == 0 else binary[:-off]

        string = ''
        binary_value = ''
        for i in binary_string:
            binary_value += i
            if binary_value in values.values():
                string += list(values.keys())[list(values.values()).index(binary_value)]
                binary_value = ''

        return string
