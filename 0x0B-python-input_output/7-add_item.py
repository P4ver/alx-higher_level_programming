#!/usr/bin/python3
"""define save and load."""
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def ld_add_sve(arg):
    """funciton that creats list either empty or full"""
    try:
        my_lst = load_from_json_file("add_item.json")
    except Exception:
        my_lst = []
    my_lst.extend(arg)
    save_to_json_file(my_lst, "add_item.json")


arg = sys.argv[1:]
ld_add_sve(arg)
