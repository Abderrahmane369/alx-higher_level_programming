#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""
import sys
import MySQLdb


def get_states():
    """Get states from database"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("""
                       SELECT * FROM states
                       ORDER BY id;
                       """)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states()
