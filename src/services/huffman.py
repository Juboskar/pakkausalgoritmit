"Huffman-algoritmin toteuttava koodi"


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


class HuffmanAlgorithm:
    "Huffman -algoritmin toteuttava luokka"

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

    def bit_values(self):
        "tallettaa merkkien huffman-koodatut bittiarvot ja palauttaa sanakirjana"
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
        values = self.bit_values()
        print(values)

    # TODO: testit!

    def decompress(self, string: str):
        "purkaa huffman algoritmilla pakatun tekstin"
