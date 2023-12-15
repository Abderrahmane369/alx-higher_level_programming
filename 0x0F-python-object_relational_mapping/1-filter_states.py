#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves states whose names start with 'N'.
It then prints the retrieved states.
"""
import sys
import MySQLdb


def main():
    """
    Connects to a MySQL database and retrieves states whose names start with 'N'.
    Prints the retrieved states.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
