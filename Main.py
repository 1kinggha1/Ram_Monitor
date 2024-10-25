"""
$python -m uvicorn Main:Ram_Api --reload
to run the main program and activate the API
"""
#Need the fastApi to make the API
from fastapi import FastAPI

#bring sqlite3 to the app
import sqlite3
#create the API and the get method of it
Ram_Api= FastAPI()
@Ram_Api.get("/{item_id}")
def present(item_id :int = 1):
    data=sqlite3.connect("DataBase.db")
    curs=data.cursor()
    #use f string to insert the numbers
    try:
        curs.execute(f"""
        SELECT * FROM system_ram
        ORDER BY timestamp DESC
        LIMIT {item_id}""")
        one_set = curs.fetchall()
        l=["timestamp","total","free","used"]
        js=[{} for i in range(item_id)]
        for i in range(len(js)):
            js[i]=dict(zip(l,one_set[i]))
    except:
        one_set="internal server error"
    finally:
        return one_set
