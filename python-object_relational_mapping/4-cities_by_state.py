#!/usr/bin/python3
"""Lists all cities with their corresponding state names."""

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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
