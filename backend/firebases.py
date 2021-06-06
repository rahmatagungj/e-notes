import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate("cred.json")
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': "https://e-notes-23-default-rtdb.firebaseio.com/"
	})

database = db.reference("/user")


   