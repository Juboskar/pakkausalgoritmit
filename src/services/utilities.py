"""Utility functions"""
import json


def list_bytes_to_list(bytes_array):
    """changes string or byetarray to list"""
    return json.loads(''.join(map(chr, bytes_array))
                      .replace("\'", "\""))
