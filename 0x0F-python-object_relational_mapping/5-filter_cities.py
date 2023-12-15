#!/usr/bin/python3
"""
Connects to a MySQL.
"""
import sys
import MySQLdb


def main():
    """
    Connects to a MySQL database and retrieves
    """

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON  states.id = cities.state_id
                   WHERE states.name = %s COLLATE utf8mb4_bin
                   ORDER BY cities.id;
                   """, (sys.argv[4] if len(sys.argv) == 5 else '',))

    for i, row in enumerate(cursor.fetchall()):
        print(row[1], end="")

        if i < cursor.rowcount - 1:
            print(", ", end="")
        else:
            print()

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
