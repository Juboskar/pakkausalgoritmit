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
        "debuggaamista helpottava tulostus"
        return f"Node: {self.symbol}: {self.value}, ({self.left}, {self.right})"


class HuffmanAlgorithm:
    "Huffman -algoritmin toteuttava luokka"

    def __init__(self):
        self.tree = None

    def compress(self, string: str):
        "pakkaa huffman algoritmilla"
        count = {}
        for i in string:
            count[i] = 1 if i not in count else count[i] + 1
        trees = [Node(symbol, value, None, None) for symbol, value in count.items()]
        while len(trees) > 1:
            min_node_1 = trees.pop(trees.index(min(trees)))
            min_node_2 = trees.pop(trees.index(min(trees)))
            trees.append(Node(None, min_node_1.value + min_node_2.value, min_node_1, min_node_2))
        self.tree = trees[0]
        print(self.tree)

    def decompress(self, string: str):
        "purkaa huffman algoritmilla pakatun tekstin"
