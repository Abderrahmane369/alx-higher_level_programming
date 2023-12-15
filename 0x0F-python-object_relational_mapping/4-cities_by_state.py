#!/usr/bin/python3
"""
Connects to a MySQL database and retrieves the cities and their corresponding states.
Prits the results.
"""
import sys
import MySQLdb


def main():
    """
    Connects to a MySQL database and retrieves the cities and their corresponding states.
    Prints the results.
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
                   ORDER BY cities.id;
                   """)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
