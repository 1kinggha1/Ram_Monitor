"""
python -m uvicorn main:app --reload
"""
#Need the fastApi to make the api
from fastapi import FastAPI
#to start recording the data 
from subprocess import Popen,run
import sqlite3
Ram_Api= FastAPI()
@Ram_Api.get("/{item_id}")
def present(item_id :int = 1):
    data=sqlite3.connect("DataBase.db")
    curs=data.cursor()
    curs.execute(f"""
    SELECT * FROM system_ram
    ORDER BY timestamp DESC
    LIMIT {item_id}""")
    one_set = curs.fetchall()
    l=["timestamp","total","free","used"]
    js=[{} for i in range(item_id)]
    for i in range(len(js)):
        js[i]=dict(zip(l,one_set[i]))
    return one_set