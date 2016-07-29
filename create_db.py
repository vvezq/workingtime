#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('workingtime.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE WORKINGTIME
       (DATE DATE,
       START_TIMESTAMP FLOAT NOT NULL,
       STOP_TIMESTAMP FLOAT NOT NULL);''')

print "Table created successfully";

conn.close()
