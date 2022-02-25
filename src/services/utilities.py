import json


def list_string_to_list(bytes_array: bytearray):
    return json.loads(''.join(map(chr, bytes_array))
                      .replace("\'", "\""))
