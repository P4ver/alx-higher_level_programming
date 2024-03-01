#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
"""
import requests
from sys import argv

if __name__ == '__main__':
    rq = requests.get(argv[1])
    st = rq.status_code
    if st < 400:
        print(rq.text)
    else:
        print("Error code: {}".format(rq.status_code))
