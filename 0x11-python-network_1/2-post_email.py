#!/usr/bin/python3
"""
script takes in a URL and an email,
sends a POST request to the passed URL with the email as a param
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    Url = sys.argv[1]
    val = {"email": sys.argv[2]}
    Data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(Url, Data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
