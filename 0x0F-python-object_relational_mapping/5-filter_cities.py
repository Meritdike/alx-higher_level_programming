#!/usr/bin/python3
"""  python script that takes in the name of a state as an
argument and lists all cities of that state """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id=states.id\
                WHERE BINARY states.name LIKE %s\
                ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cur.fetchall()
    temp = [row[0] for row in rows]
    print(", ".join(temp))
