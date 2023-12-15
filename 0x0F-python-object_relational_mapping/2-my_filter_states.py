#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves rows from the 'states' table
based on a given name.
"""
import sys
import MySQLdb


def main():
    """
    This function connects to a MySQL database and retrieves rows from the 'states' table
    based on a given name. It takes command line arguments for the database credentials
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
        "SELECT * FROM states WHERE name='{}' ORDER BY id;".format(sys.argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
