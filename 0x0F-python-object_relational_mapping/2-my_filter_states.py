#!/usr/bin/python3
"""
Script takes in an arg and displays all values in the states,
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nmeSr)

    s = cur.fetchall()
    for q in s:
        print(q)
    cur.close()
    db.close()
