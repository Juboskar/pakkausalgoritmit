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
        values = self.bit_values()
        print(values)

        """" todo puun tallennus toteuttamatta vielä
            1  huffman puun pituus (n)
            n puu
            1 koodatun tekstin pituus (m) | edit: tai oikeastaan off kannattanee tallentaa
            m data
        """
        # seuraava pätkä on PAHASTI kesken ja lähinnä sandbox testailua

        binary = ''.join([values[i] for i in string])
        print(binary)
        n = len(binary)
        off = 0 if 8 - (n % 8) == 8 else 8 - (n % 8)
        binary += off * '0'
        integer_values = [off]
        for i in range(0, n, 8):
            integer_values.append(int(binary[i:i + 8], 2))

        # str(values).encode('ascii') olkoon väliaikainen,
        # perehdytään myöhemmin onko järkevämpiä tapoja pakata sanakirja

        m = len(str(values))
        return bytearray([m]) + bytearray(str(values).encode('ascii')) + bytearray(integer_values)
        #
        # todo palauttaa tallennettavaksi

    def decompress(self, bytes: bytearray):
        "purkaa huffman algoritmilla pakatun tekstin"
        bytes_to_int = list(bytes)
        print(bytes_to_int)
        m = bytes_to_int[0]

        # muunnetaan dictionaryksi
        values = json.loads(bytes[1:m + 1].decode('ascii').replace("\'", "\""))

        off = bytes_to_int[m + 1]
        print(off)
        s = ''
        for i in bytes_to_int[m + 2:]:
            s += "{0:b}".format(i).zfill(8)
        binary = s if off == 0 else s[:-off]
        print(binary)

        string = ''
        c = ''
        for i in binary:
            c += i
            if c in values.values():
                string += list(values.keys())[list(values.values()).index(c)]
                c = ''

        return string
