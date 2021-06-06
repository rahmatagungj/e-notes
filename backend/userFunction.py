from firebases import database_user

def update_user(username,password):
     database_user.update({
        str(username):
        {
            "password": str(password)
        }
    })


def delete_user(username):
    database_user.child(username).set({})


def get_user(username):
    for key, value in database_user.get().items():
        print(key,username)
        if username == key:
            return "yes"
        else:
            continue
            return "nope"
        
        
def login_user(username,password):
    for key, value in database_user.get().items():
        if str(username) == str(key) and str(value["password"]) == str(password):
            return "yes"
        else:
            continue
            return "nope"