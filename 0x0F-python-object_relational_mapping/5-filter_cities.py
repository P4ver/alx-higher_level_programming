#!/usr/bin/python3
"""
argument and lists all cities of that state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    cursor = db.cursor()

    cursor.execute(
        "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ASC", (state_name,)
    )

    res = cursor.fetchone()

    if res:
        print(res[0])
    else:
        print("No cities found for the specified state")

    cursor.close()
    db.close()
