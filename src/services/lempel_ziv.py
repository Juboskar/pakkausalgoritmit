"Lempel-Ziv -algoritmin toteuttava koodi"

import json


class LzAlgorithm:
    "Lempel-Ziv -algoritmin toteuttava luokka"  # todo refaktoroi järkevämmäksi

    def __init__(self):
        pass

    def compress(self, string: str):
        "pakkaa lempel-ziv algoritmilla"
        initial = list(set(string))
        string_list = initial.copy()

        output = []
        s = ''
        for c in string:
            if s + c in string_list:
                s += c
            else:
                output.append(string_list.index(s))
                string_list.append(s + c)
                s = c
        output.append(string_list.index(s))
        print(initial)
        print(string_list)
        print(output)

        encoded_values = bytearray(str(initial).encode('ascii'))
        header = len(encoded_values).to_bytes(4, 'big')

        return header + bytearray(str(initial).encode('ascii')) + bytearray(output)
        # fixme output indexit menee tod näk yli byten

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
        output = ''
        for i in bytes_int_values[values_length + 4:]:
            print(" - ", i)
            c = values[i]
            if s + c in values:
                s += c
            else:
                output += s
                values.append(s + c)
                s = c
        output += s

        print(values)

        print(output)
        return output
