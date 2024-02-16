#!/usr/bin/python3
"""list all the cities in a specific state"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    data = cur.fetchall()
    result = list(line[0] for line in data)
    print(*result, sep=", ")
    cur.close()
    db.close()
