#!/usr/bin/python3
"""Lists all cities belonging to a state provided by the user."""

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
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    connection.close()
