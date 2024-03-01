#!/usr/bin/python3
"""
A script takes in a letter and sends POST req
to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    lttr = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": lttr}

    rq = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = rq.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
