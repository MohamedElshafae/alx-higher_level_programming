#!/usr/bin/python3
"""doc"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    v = ""
    if len(argv) > 1:
        v = argv[1]
    data = {
        'q': v
    }
    response = post('http://0.0.0.0:5000/search_user', data)
    try:
        json_res = response.json()
        if json_res:
            print(f'[{json_res.get("id")}] {json_res.get("name")}')
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
