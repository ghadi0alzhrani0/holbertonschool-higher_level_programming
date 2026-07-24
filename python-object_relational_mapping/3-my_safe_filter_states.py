#!/usr/bin/python3
"""Safely lists states that match a user-provided state name."""

import sys
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    state_name = sys.argv[4]
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
