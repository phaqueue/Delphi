import json
import csv
import re
import random
import ast

poss_f_names = [
    "Daniel",
    "John",
    "Josh",
    "Ralph",
    "Chris",
    "Julia",
    "Suzanne",
    "Michelle",
    "Britney",
    "Jessica"
]

poss_l_names = [
    "Smith",
    "Brown",
    "Johnson",
    "Williams",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Martinez",
    "Moore"
]
poss_filters = [
    "Vegan",
    "Beef",
    "Pork",
    "Nuts",
    "Sweet"
]

def create_user(k=10, hater=False, easy=False, allergic=False):
    ids = random.sample(range(1, 99999), k)
    users = {}
    user = {}
    for n, i in enumerate(ids):
        user["user_id"] = i
        user["bluetooth_id"] = None
        user["name"] = {
            "first_name" : poss_f_names[random.randint(0, len(poss_f_names) - 1)],
            "last_name" : poss_l_names[random.randint(0, len(poss_l_names) - 1)]
        }
        user["email"] = user["name"]["first_name"] + "." + user["name"]["last_name"] + str(random.randint(1, 999)) + "@gmail.com"
        user["preferences"] = {
            "calories" : random.randint(1, 10),
            "protein" : random.randint(1, 10),
            "fat" : random.randint(1, 10),
            "carbohydrates": random.randint(1, 10),
            "sugars" : random.randint(1, 10)
        }
        user["filters"] = random.sample(poss_filters, k=random.randint(0, len(poss_filters)))
        users[n] = user.copy()

    if hater:
        users[len(users)] = {
            "user_id":100000,
            "bluetooth_id":None,
            "name":{"first_name":"Hater", "last_name":"McHate"},
            "email":"idontlikefood@gmail.com",
            "preferences":{
                "calories" : 0,
                "protein" : 0,
                "fat" : 0,
                "carbohydrates": 0,
                "sugars" : 0
            },
            "filters":[]
        }

    if easy:
        users[len(users)] = {
            "user_id":100001,
            "bluetooth_id":None,
            "name":{"first_name":"Hater", "last_name":"McHate"},
            "email":"miam@gmail.com",
            "preferences":{
                "calories" : 10,
                "protein" : 10,
                "fat" : 10,
                "carbohydrates": 10,
                "sugars" : 10
            },
            "filters":[]
        }

    if allergic:
        users[len(users)] = {
            "user_id":100002,
            "bluetooth_id":None,
            "name":{"first_name":"Allergic", "last_name":"Customer"},
            "email":"allergies@gmail.com",
            "preferences":{
                "calories" : random.randint(1, 10),
                "protein" : random.randint(1, 10),
                "fat" : random.randint(1, 10),
                "carbohydrates": random.randint(1, 10),
                "sugars" : random.randint(1, 10)
            },
            "filters":poss_filters.copy()
        }

    with open("NOSQL/users.json", "w") as f:
        json.dump(users, f, indent=4)
    


if __name__ == "__main__":
    create_user()


    