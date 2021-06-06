from firebases import database

def update_user(id,name):
     database.update({
        str(name):
        {
            "id": int(id)
        }
    })

def delete_user(name):
    database.child(name).set({})