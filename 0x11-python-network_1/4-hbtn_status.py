#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    Url = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(Url.text)))
    print("\t- content: {}".format(Url.text))
