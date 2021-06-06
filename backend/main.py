from typing import Optional
import os
from fastapi import FastAPI
import userFunction 
from firebases import database_user
import uvicorn

app = FastAPI(docs_url="/helpme", redoc_url=None)

@app.get("/")
def home():
    return {"API": "Works"}


@app.get("/create_user/{username}")
def create_user(username: str, password: str):
    try: 
        userFunction.update_user(username,password)
        return {"Sucess": username}
    except:
        return {"error"}

@app.get("/delete_user/{username}")
def delete_user(username: str):
    try: 
        userFunction.delete_user(username)
        return {"Deleted": username}
    except:
        return {"User Not Found"}


@app.get("/get_user/{username}")
def get_user(username: str):
    if userFunction.get_user(username) == "yes":
        return {"Result": username}
    else:
        return {"User Not Found"}
   

@app.get("/login_user/{username}")
def login_user(username: str, password: str):
    if userFunction.login_user(username,password) == "yes":
        return {"isSuccess": "true"}
    else:
        return {"isSuccess": "false"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)