"Lempel-Ziv ja Huffman -algoritmit toteuttava koodi"


class CompressingAlgorithm:
    "Algoritmirajapinta"

    def __init__(self):
        pass

    def compress(self, string):
        "Abstrakti pakkausfunktio"

    def decompress(self, string):
        "Abstrakti pakkausfunktio"


class LzAlgorithm(CompressingAlgorithm):
    "Lempel-Ziv -algoritmin toteuttava luokka"

    def __init__(self):
        super().__init__()

    def compress(self, string):
        "pakkaa lempel-ziv algoritmilla"
        print(string)


class HuffmanAlgorithm(CompressingAlgorithm):
    "Lempel-Ziv -algoritmin toteuttava luokka"

    def __init__(self):
        super().__init__()
