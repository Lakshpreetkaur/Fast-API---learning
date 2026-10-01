# creating api bassically we will create endpoint when uswr hit that endpoint it shows HELLO WORLD
#  Creating HELLO WORLD api 

from fastapi import FastAPI

app =FastAPI()

#  Defining endpoint 

# 1. Defining route /path
@app.get("/")

# 2. creating func for this endpoint 
def hello():
  return {'message':'hello World'}

@app.get('/about')
def about():
  return {"message":"I'm learning Fast API"}
