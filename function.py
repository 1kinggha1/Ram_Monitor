# import The sqlite3 Framework To keep Record
import sqlite3
#Needs To Be Installed, Tells How Much Of The Ram Is Total Or Free Or Taken, Highly Compatible With A Lot Of Os Like Linux
import psutil
#Need This For The Epoch (timestamp) And Delays
import time
"""
This part takes the time in milliseconds, the total, used, and free RAM in MBs, and makes a dictionary out of them.
                    Later, it will be used in the API for sending the last N recent records.
"""
def System_Ram_Update():
    return {"timestamp":int(time.time()),
            "total":psutil.virtual_memory().total//1024**2
            ,"free":psutil.virtual_memory().free//1024**2
            ,"used":psutil.virtual_memory().used//1024**2}

DataBase = sqlite3.connect("DataBase.db")
cur=DataBase.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTs system_ram (
        timestamp INTEGER PRIMARY KEY,
        total INTEGER,
        free INTEGER,
        used INTEGER
    )
''')
cur.execute('''
    INSERT INTO system_ram (timestamp, total, free, used)
    VALUES (?,?, ?, ?)
''', (list(System_Ram_Update().values())))
DataBase.commit()
cur.close()