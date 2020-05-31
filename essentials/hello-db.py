#!/usr/bin/env python3

import sqlite3


# Python DB API serves as a common consolidated interface for different dbs instances
def main():
    print('connect')
    db = sqlite3.connect('db-api.db')  # db file
    cur = db.cursor()  # grab a cursor from the db handle

    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)

    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)

    print('commit')
    db.commit()

    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')

    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)

    print('drop')
    cur.execute("DROP TABLE test")

    print('close')
    db.close()


if __name__ == '__main__':
    main()

# CONSOLE OUTPUT: