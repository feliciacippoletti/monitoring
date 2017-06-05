#!/usr/bin/python

import MySQLdb

def connectMySQL(db_name):

    try:

        conn = MySQLdb.connect(host="localhost",
                     user="root",
                     #passwd="test",
                     db=db_name)

        cur = conn.cursor()

        return conn, cur
    
    except MySQLdb.Error:
     print "Connection Failed"
     return False

def findLocks():
    cur.execute("SELECT * FROM INNODB_LOCK_WAITS")
    results = cur.fetchone()
    print results

conn, cur = connectMySQL("information_schema")
findLocks()
