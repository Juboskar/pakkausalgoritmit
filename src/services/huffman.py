"Huffman-algoritmin toteuttava koodi"
import json


class Node:
    "Huffman-puun solmun totetuttava luokka"

    def __init__(self, symbol, value, left, right):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, comparable):
        "pienimmän arvon omaavan solmun löytämistä varten"
        return self.value < comparable.value

    def __str__(self):
        "debuggaamista helpottava str muoto"
        return f"Node: {self.symbol}: {self.value}, ({self.left}, {self.right})"


class HuffmanCompressor:
    "Huffman pakkauksen toteuttava luokka"

    def __init__(self):
        self.tree = None

    def build_tree(self, string: str):
        "rakentaa huffman-puun"
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
        "etsii merkkien huffman-koodatut bittiarvot ja palauttaa sanakirjana"
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
        "pakkaa huffman algoritmilla"
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
        x = len(encoded_values).to_bytes(4, 'big')
        return x + bytearray(str(values).encode('ascii')) + bytearray(integer_values)


class HuffmanDecompressor:
    "Huffman -algoritmin toteuttava luokka"

    def __init__(self):
        self.values_length = None

    def __calculate_values(self, bytes_array: bytearray):
        return json.loads(''.join(map(chr, bytes_array[4:self.values_length + 4])).replace("\'", "\""))

    def decompress(self, bytes_array: bytearray):
        "purkaa huffman algoritmilla pakatun tekstin"
        self.values_length = int.from_bytes(bytes_array[0:4], 'big')
        values = self.__calculate_values(bytes_array)

        bytes_int_values = list(bytes_array)
        off = bytes_int_values[self.values_length + 4]
        s = "".join(map(lambda x: "{0:b}".format(x).zfill(8), bytes_int_values[self.values_length + 5:]))

        binary = s if off == 0 else s[:-off]  # en ymmärrä miten s[:-0] toimii

        string = ''
        c = ''
        for i in binary:
            c += i
            if c in values.values():
                string += list(values.keys())[list(values.values()).index(c)]
                c = ''

        return string
