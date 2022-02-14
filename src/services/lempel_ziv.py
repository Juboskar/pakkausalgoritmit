"Lempel-Ziv -algoritmin toteuttava koodi"


class LzAlgorithm:
    "Lempel-Ziv -algoritmin toteuttava luokka"

    def __init__(self):
        pass

    def compress(self, string: str):
        "pakkaa lempel-ziv algoritmilla"
        string_dict = {c: list(set(string)).index(c) for c in set(string)}
        print(string_dict)

        output = []
        s = ''
        for c in string:
            if s + c in string_dict.keys():
                s += c
            else:
                output.append(string_dict[s])
                string_dict[s + c] = len(string_dict)
                s = c
        output.append(string_dict[s])
        print(string_dict)
        print(output)

    def decompress(self, string: str):
        "purkaa lempel-ziv algoritmilla pakatun tekstin"



