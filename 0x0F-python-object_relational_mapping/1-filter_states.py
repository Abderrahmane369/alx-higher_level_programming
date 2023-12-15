#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieve.
It then prints the retrieved states.
"""
import sys
import MySQLdb


def main():
    """
    Prints the retrieved states.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_bin ORDER BY id;")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
