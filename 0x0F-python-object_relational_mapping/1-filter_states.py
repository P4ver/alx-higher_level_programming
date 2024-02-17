#!/usr/bin/python3
"""
Script that lists all states starting with N
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    s = cur.fetchall()
    for q in s:
        print(q)
    cur.close()
    db.close()
