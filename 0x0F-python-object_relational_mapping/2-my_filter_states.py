#!/usr/bin/python3
"""list all the states that match the last argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    data = cur.fetchall()
    for line in data:
        print(line)
    cur.close()
    db.close()
