#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    data = {
        'email' : argv[2]
    }
    data = parse.urlencode(data).encode('utf-8')
    with request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
