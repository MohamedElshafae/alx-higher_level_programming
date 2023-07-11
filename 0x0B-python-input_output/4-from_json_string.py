#!/usr/bin/python3
""" .... """


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON"""
    import json
    data = json.loads(my_str)
    return data
