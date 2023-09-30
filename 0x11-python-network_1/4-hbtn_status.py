#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from requests import get

    response = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
