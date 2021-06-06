from typing import Optional
import os
from fastapi import FastAPI
import userFunction 

app = FastAPI(docs_url="/helpme", redoc_url=None)

@app.get("/")
def read_root():
    return {"API": "Works"}


@app.get("/create_user/{id}")
def read_item(id: int, name: Optional[str] = None):
    try: 
        userFunction.update_user(id,name)
        return {"id": id, "name": name}
    except:
        return {"error"}

@app.get("/delete_user/{name}")
def read_item(name: str):
    try: 
        userFunction.delete_user(name)
        return {"Deleted": name}
    except:
        return {"User not found"}

# run here
# uvicorn main:app --reload