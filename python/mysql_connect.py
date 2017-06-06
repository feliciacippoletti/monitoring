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
    #check if metadata_locks has any rows
    cur.execute("SELECT ENABLED, TIMED FROM setup_instruments WHERE NAME = 'wait/lock/metadata/sql/mdl'")

    results = cur.fetchone()
    print results
    if 'NO' in results:
        print 'disabled'

        cur.execute("UPDATE setup_instruments SET ENABLED = 'YES', TIMED = 'YES' WHERE NAME = 'wait/lock/metadata/sql/mdl';")
        results = cur.fetchone()
        print results

    else:
        cur.execute("SELECT * FROM metadata_locks where LOCK_STATUS = 'PENDING'")
        results = cur.fetchone()
        #if 'None' in results:
         #   return
        #else:
            #send email to team notifying of hang, possible query/job is hanging
         #   return

conn, cur = connectMySQL("performance_schema")
findLocks()
