#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    url = argv[1]
    data = {
        'email': argv[2]
    }
    response = post(url, data)
    print(response.text)
