from pymongo import MongoClient
from pymongo.collection import ObjectId
import bcrypt
import math
import json

import requests

client = MongoClient("mongodb+srv://user:pwd@cluster0.x4ft0.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.get_database("data")

def register_user(email, password, spotify, lat, lon):
    if db.users.find_one({"email":email}) == None:
        hashp = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        k = {"email":email, "password":hashp, "spotify":spotify, "lat":lat, "lon":lon, "manager":""}
        db.users.insert_one(k)
        return {"status":"success"}
    else:
        return {"status":"failed"}

def login_user(email, password):
    k = db.users.find_one({"email":email})

    if k != None:
        x = bcrypt.hashpw(password.encode('utf-8'), k["password"])
        
        
        if x == k["password"]:
            return {"status":"success"}
        else:
            return {"status":"failed"}

    else:
        return {"status":"failed"}

def update_location(lat, lon, email):
    try:
        db.users.update_one({"email":email}, {"$set":{"lat":lat}})
        db.users.update_one({"email":email}, {"$set":{"lon":lon}})
        return {"status":"success"}
    except:
        return {"status":"failed"}

def get_songs(email):
    k = db.users.find_one({"email":email})
    if k["manager"] == "":
        return []
    else:
        return db.managers.find_one({"email":k["manager"]})["songs"]
