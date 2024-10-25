#needs to be installed, tells how much of the ram is total or free or taken, highly compatible with a lot of OS like linux
import psutil
#need this for the epoch (timestamp)
import time
"""
this part takes the time in ms , the toatal, used, free Ram in MB and makes a dictionary out of them.
                                    later to be used in the main.py file
"""
def System_Ram_Update():
    return {"timestamp":int(time.time()),
            "total":psutil.virtual_memory().total//1024**2
            ,"free":psutil.virtual_memory().free//1024**2
            ,"used":psutil.virtual_memory().used//1024**2}