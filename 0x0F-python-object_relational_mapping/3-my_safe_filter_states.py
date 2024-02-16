#!/usr/bin/python3
"""same as the previous with better syntax"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    pattern = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (pattern, ))
    data = cur.fetchall()
    for line in data:
        print(line)
    cur.close()
    db.close()
