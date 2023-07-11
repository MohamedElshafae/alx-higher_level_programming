#!/usr/bin/python3
"""..."""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters"""
    with open(filename, mode="w", encoding='utf-8') as file:
        num_of_bytes = file.write(text)
        file.close()
        return num_of_bytes
