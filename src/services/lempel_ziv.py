"Lempel-Ziv -algoritmin toteuttava koodi"

import json


class LzAlgorithm:
    "Lempel-Ziv -algoritmin toteuttava luokka"  # todo refaktoroi järkevämmäksi

    def __init__(self):
        pass

    def compress(self, string: str):
        "pakkaa lempel-ziv algoritmilla"
        initial_dict = {c: list(set(string)).index(c) for c in set(string)}
        string_dict = initial_dict.copy()

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
        print(initial_dict)
        print(string_dict)
        print(output)

        encoded_values = bytearray(str(initial_dict).encode('ascii'))
        header = len(encoded_values).to_bytes(4, 'big')
        return header + bytearray(str(initial_dict).encode('ascii')) + bytearray(output)

    def calculate_values(self, bytes_array: bytearray, values_length):  # sama kun huffmanin kanssa, voisi yhdistää
        """palauttaa sanakirjan"""

        return json.loads(''.join(map(chr, bytes_array[4:values_length + 4]))
                          .replace("\'", "\""))

    def decompress(self, bytes_array: str):
        "purkaa lempel-ziv algoritmilla pakatun tekstin"
        print(bytes_array)
        values_length = int.from_bytes(bytes_array[0:4], 'big')
        values = self.calculate_values(bytes_array, values_length)
        print(values)
        bytes_int_values = list(bytes_array)
        print(bytes_int_values[values_length + 4:])
        s = ''
        

        print(values)

        return "HELLO"
