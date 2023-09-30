#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from urllib import request
    from sys import argv

    url = argv[1]
    with request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])
