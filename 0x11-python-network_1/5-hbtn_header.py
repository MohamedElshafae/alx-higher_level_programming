#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = argv[1]
    response = get(url)
    print(response.headers['X-Request-Id'])
