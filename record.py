# Import the sqlite3 Framework To Keep the Record
import sqlite3

#Needs To Be Installed, Tells How Much Of The Ram Is Total Or Free Or Taken, Highly Compatible With A Lot Of Os Like Linux
from psutil import virtual_memory as Ram

#Need This For The Epoch (timestamp) And Delays
from time import time,sleep

"""
This part takes the time in seconds, the total, used, and free RAM in MBs, and makes a List out of them.
                    Later, it will be used in the API for sending the last N recent records.
"""
def System_Ram_Update():
    return [int(time())
            ,Ram().total//1024**2
            ,Ram().free//1024**2
            ,Ram().used//1024**2]

#Create A sqlite3 DataBase And Add The Columns To It, Setting The Epoch Time As The Primary Key.
#if it already exists connect to it
DataBase = sqlite3.connect("DataBase.db")
cur=DataBase.cursor()
#if the table does not exist already, make one
cur.execute('''
    CREATE TABLE IF NOT EXISTs system_ram (
        timestamp INTEGER PRIMARY KEY,
        total INTEGER,
        free INTEGER,
        used INTEGER
    )
''')


#Insert Data Inside the Respective Columns.
while True:
    #just to make sure that the time difference is always approximately 5 seconds
    start=time()
    cur.execute('''
        INSERT INTO system_ram (timestamp, total, free, used)
        VALUES (?,?, ?, ?)
    ''', System_Ram_Update())
    DataBase.commit()
    end=time()
    sleep(60-(end-start))
cur.close()
