#!/usr/bin/python3
"""
sends a POST request to a given URL with a given email.
"""
import sys
import requests


if __name__ == "__main__":
    Url = sys.argv[1]
    val = {"email": sys.argv[2]}

    rq = requests.post(Url, data=val)
    print(rq.text)
