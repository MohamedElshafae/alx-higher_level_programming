#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
if __name__ == '__main__':
    """
    Access to the database
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")

    cur = conn.cursor()
    cur.execute("\
        SELECT\
            cities.id, cities.name\
        FROM\
            cities\
        JOIN\
            states\
        ON\
            cities.state_id = states.id\
        WHERE\
            states.name LIKE '{}'\
        ".format(sys.argv[4]))

    query_rows = cur.fetchall()
    if query_rows is not None:
        print(", ".join([row[1] for row in query_rows]))
    cur.close()
    conn.close()
