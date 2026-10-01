# creating api bassically we will create endpoint when uswr hit that endpoint it shows HELLO WORLD
#  Creating HELLO WORLD api 

from fastapi import FastAPI
import json 

app =FastAPI()

#  to load patient dataset -> this func will return the entire data of patients on calling this func
def load_data():
  with open('patients.json' ,'r') as f:
    data = json.load(f)

  return data

#  Defining endpoint 

# 1. Defining route /path
@app.get("/")

# 2. creating func for this endpoint 
def hello():
  return {'message':'Patient Management System API'}

@app.get('/about')
def about():
  return {"message":"Fully Functional API to manage your patient records"}

# to give patient data to our client
@app.get('/view')
def view():
  data = load_data()

  return data

