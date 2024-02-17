#!/usr/bin/python3
"""
Script takes in an arg and displays all values in the states,
"""

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    s = cursor.fetchall()
    for ste in s:
        print(ste)
    cursor.close()
    db.close()
