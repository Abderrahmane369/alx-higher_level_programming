#!/usr/bin/python3
"""
This module connects ents for the database credentials
and the name to filter by.
"""
import sys
import MySQLdb


def main():
    """
    This function connects to a MySQL dand atabase credentials
    and the name to filter by.
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id;", (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
