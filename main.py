from fastapi import FastAPI
import os

app=FastAPI()
#return albums for a particular band
@app.get("/get")
def getBandbyID():
 return "Hello World from India "