"Huffman -algoritmin toteuttava koodi"


class Node:
    "Huffman-puun solmun totetuttava luokka"

    def __init__(self, symbol, value, left, right):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, comparable):
        return self.value < comparable.value

    def __str__(self):
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
        forest = [Node(symbol, value, None, None) for symbol, value in count.items()]
        min_value_1 = forest.pop(forest.index(min(forest)))
        min_value_2 = forest.pop(forest.index(min(forest)))
        print(min_value_1)
        print(min_value_2)

        # todo: tallenna puu, myös tallenna purkua varten tiedostoon compressorissa sitten myös
        self.tree = None

    def decompress(self, string: str):
        "purkaa huffman algoritmilla pakatun tekstin"
