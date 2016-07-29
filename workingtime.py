from datetime import datetime as dt
import datetime
import time
from time import mktime
import sqlite3

# function to convert seconds to HH:MM:SS
def seconds_to_string(t):
    return datetime.timedelta(seconds=t)

# function to get seconds since epoch
def sec_since_epoch():
    dt_start = dt.now()
    return mktime(dt_start.timetuple()) + dt_start.microsecond / 1000000.0

# open db
conn = sqlite3.connect('workingtime.db')
cursor = conn.cursor()

# make this work with Python2 or Python3
try: input = raw_input
except: pass

# get date
date = time.strftime("%Y-%m-%d")

# check if entry for today already exists
sql = "SELECT * FROM WORKINGTIME WHERE DATE=?"
cursor.execute(sql, [(date)])
check = cursor.fetchall()
conn.commit()

if check:
    print ("Entry for today already exists")
    exit()

# start program
print ("=====================================\n")
print ("==== SIMPLE WORKING TIME COUNTER ====\n")
print ("=====================================\n")

e = input("Start counter by pressing Enter or give time in HH:MM: ")

# check if time was given and set starting time accordingly
# else use current time
if e != "":
    time_string = "%s %s" % (date, e)
    timedt = dt.strptime(time_string, "%Y-%m-%d %H:%M")
    sec_since_epoch_start = mktime(timedt.timetuple()) + timedt.microsecond / 1000000.0
else:
    # start counting
    sec_since_epoch_start = sec_since_epoch()

# run loop that shows elapsed time
while True:
    choice = input('Stop counter by pressing Enter. Press any other key to see elapsed time. ')
    # check if Enter is pressed, break loop if true
    if choice == "":
        break
    else:
        # show elapsed time
        sec_since_epoch_status = sec_since_epoch()
        elapsed_status = sec_since_epoch_status - sec_since_epoch_start
        print (seconds_to_string(elapsed_status))

# end counting
sec_since_epoch_end = sec_since_epoch()

# print final elapsed time
elapsed_time = sec_since_epoch_end - sec_since_epoch_start
print (seconds_to_string(elapsed_time))

# insert data to db
conn.execute('INSERT INTO WORKINGTIME (DATE, START_TIMESTAMP, STOP_TIMESTAMP) \
VALUES (?, ?, ?)', (date,sec_since_epoch_start, sec_since_epoch_end))
conn.commit()
print ("ALL DONE.")

# close db
conn.close()
