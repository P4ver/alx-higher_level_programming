#!/usr/bin/python3
"""
script that takes 2 arg in order to solve this challenge,
"""
import sys
import requests


if __name__ == "__main__":
    Url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rq = requests.get(Url)
    cmmit = rq.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                cmmit[i].get("sha"),
                cmmit[i].get("commit").get("author").get("name")))
    except Exception:
        pass
