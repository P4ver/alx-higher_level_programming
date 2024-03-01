#!/usr/bin/python3
""" 
script that takes in a URL, send a request to URL, and dispaly body,
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as Err:
        print('Error code:', Err.code)
