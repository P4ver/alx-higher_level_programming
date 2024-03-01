#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    Url = sys.argv[1]

    rq = requests.get(Url)
    print(rq.headers.get("X-Request-Id"))
