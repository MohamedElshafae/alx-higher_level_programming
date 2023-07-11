#!/usr/bin/python3
""" .... """


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    import json
    data = json.dumps(my_obj)
    return data
