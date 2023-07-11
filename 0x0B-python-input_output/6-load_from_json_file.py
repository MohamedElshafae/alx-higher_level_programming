#!/usr/bin/python3
""" ... """


def load_from_json_file(filename):
    """  creates an Object from a “JSON file”: """
    with open(filename, mode="r", encoding="utf-8") as file:
        import json
        my_object = json.load(file)
        file.close()
        return my_object
