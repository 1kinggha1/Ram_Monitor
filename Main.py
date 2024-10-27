"""
$python -m uvicorn Main:Ram_Api --reload
to run the main program and activate the API
"""
import uvicorn
#Need the fastApi to make the api
from fastapi import FastAPI
#to start recording the data
#from subprocess import Popen,run
#bring sqlite3 to the app
import sqlite3
#create the api and the get method of it
Ram_Api= FastAPI()
@Ram_Api.get("/")
def null_adress():
    return "please add /n at the end of the Url (n being the number of the records)"
@Ram_Api.get("/{item_id}")
def present(item_id :int = 1):
    Data=sqlite3.connect("DataBase.db")
    curs=Data.cursor()
    #use f string to insert the numbers
    try:
        curs.execute(f"""
        SELECT * FROM system_ram
        ORDER BY timestamp DESC
        LIMIT {item_id}""")
        Raw_data = curs.fetchall()
        l=["timestamp","total","free","used"]
        Formatted_data=[{} for i in range(item_id)]
        for i in range(len(Formatted_data)):
            Formatted_data[i]=dict(zip(l,Raw_data[i]))
    except:
        #error handling
        curs.execute("SELECT COUNT(*) FROM system_ram")
        count = curs.fetchone()[0]
        if item_id>count:
            # only show available data
            Formatted_data.insert(0,f"we only have {count} record:")
            Formatted_data=Formatted_data[0:count+1]
        else:
            #unknown error
            Formatted_data="There might be an internal error"
    finally:
            #finally, send out the data
        return Formatted_data
        curs.close()
