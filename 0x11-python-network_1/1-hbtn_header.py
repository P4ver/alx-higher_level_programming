#!/usr/bin/python3
"""
The "X-Request-Id" header plays a crucial role in tracking requests,
within a web application
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
