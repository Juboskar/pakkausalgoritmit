from services.compress_algorithms import LzAlgorithm, HuffmanAlgorithm

lz = LzAlgorithm()
huff = HuffmanAlgorithm()


def compress_file(file, selected_algorithm):
    """Avaa tiedoston ja antaa sisällön merkkijonona Lempel-Ziv algoritmilla pakkaavalle luokalle"""
    with open(file) as file:
        if selected_algorithm == "lz":
            lz.compress(file.read())
        elif selected_algorithm == "huff":
            huff.compress(file.read())


def return_decompressed(packed_file):
    pass
