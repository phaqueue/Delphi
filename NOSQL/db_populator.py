import pymongo
import json
from pymongo import MongoClient, InsertOne
from user_creator import create_user

client = pymongo.MongoClient("mongodb+srv://naelbelhaj:Bloume2003@cluster0.8xvrjlp.mongodb.net/test")

create_user(10, True, True, True)

db = client["delphi"]
users = db["users"]
res = db["restaurants"]
requesting = []

db.users.drop()
res.drop()

with open(r"NOSQL/users.json") as f:
    myDict = json.load(f)
    for i in myDict.values():
        requesting.append(InsertOne(i))

result = users.bulk_write(requesting)

requesting = []

with open(r"NOSQL/restaurants.json") as f:
    myDict = json.load(f)
    res.insert_one(myDict)

#result = res.bulk_write(requesting)

client.close()
