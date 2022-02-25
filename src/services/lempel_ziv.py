"Lempel-Ziv -algoritmin toteuttava koodi"

import json
from services.utilities import list_string_to_list


class LzCompressor:
    "Lempel-Ziv -algoritmin toteuttava luokka"  # todo refaktoroi järkevämmäksi

    def __init__(self):
        pass

    def compress(self, string: str):
        "pakkaa lempel-ziv algoritmilla"
        initial = sorted(list(set(string)))  # sorted testejä varten
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

        encoded_values = bytearray(str(initial).encode('ascii'))
        header = len(encoded_values).to_bytes(4, 'big')

        arr = header + bytearray(str(initial).encode('ascii'))
        o = [i.to_bytes(2, byteorder='big') for i in output]
        for i in o:
            arr += i
        return arr


class LzDecompressor:
    "Lempel-Ziv -algoritmin toteuttava luokka"  # todo refaktoroi järkevämmäksi

    def __init__(self):
        pass

    def decompress(self, bytes_array: str):
        "purkaa lempel-ziv algoritmilla pakatun tekstin"
        values_length = int.from_bytes(bytes_array[0:4], 'big')
        values = list_string_to_list(bytes_array[4:values_length + 4])

        # todo tääl vois vähän uudelleennimetä muuttujia ja pilkkoo pienempiin metodeihin

        bytes_int_values = list(bytes_array)

        x = bytes_int_values

        b = []
        i = values_length + 4
        while i < len(x):
            b.append(int.from_bytes(bytes_array[i:i + 2], 'big'))
            i += 2
        print(b)

        c = values[b.pop(0)]
        output = c
        for i in b:
            if i < len(values):
                s = values[i]
            else:
                s = c + c[0]
            output += s
            values.append(c + s[0])
            c = s

        return output
