#!/usr/bin/python3
"""function"""


def text_indentation(text):
    """..."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.strip().replace('. ', '.\n\n').replace('? ', '?\n\n').replace(': ', ':\n\n')
    print(new_text, end="")
