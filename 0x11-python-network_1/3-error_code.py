#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from urllib import request, parse, error
    from sys import argv

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
