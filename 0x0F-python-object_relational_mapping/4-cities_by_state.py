#!/usr/bin/python3
"""script that lists all cities from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities JOIN "
        "states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    cties = cursor.fetchall()

    for c in cties:
        print(c)

    cursor.close()
    db.close()
