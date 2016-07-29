from datetime import datetime as dt
import datetime
from time import mktime
import sqlite3

# function to convert seconds to HH:MM:SS
def seconds_to_string(t):
    return datetime.timedelta(seconds=t)

# function to check that date format is correct
def validate_date(d):
    try:
        dt.strptime(d, '%Y-%m-%d')
    except ValueError:
        raise

# get seconds since epoch
def sec_since_epoch():
    dt_start = dt.now()
    return mktime(dt_start.timetuple()) + dt_start.microsecond / 1000000.0

# open db
conn = sqlite3.connect('workingtime.db')
cursor = conn.cursor()

# make this work with Python2 or Python3
try: input = raw_input
except: pass

# Get date
date = input("Give date in format YYYY-MM-DD: ")

validate_date(date)

# Use date to get values from db
sql = "SELECT * FROM WORKINGTIME WHERE DATE=?"
cursor.execute(sql, [(date)])
check = cursor.fetchone()
conn.commit()

# calculate elapsed time
sec_since_epoch_start = check[1]
sec_since_epoch_end = check[2]
elapsed_status = sec_since_epoch_end - sec_since_epoch_start
human_elapsed_status = seconds_to_string(elapsed_status)
print ("Your working time for %s was %s (HH:MM:SS)" % (date, human_elapsed_status))

# close db
conn.close()
