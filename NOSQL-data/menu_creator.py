import json
import csv
import re
import requests
import time

"""
Still working on grabbing ingredients using an API
"""

drink_ingredients = {
    "Beverages": ["Ice", "Water", "Sugar"],
    "Coffee & Tea": ["Sugar", "Cream", "Caffeine"],
    "Smoothies & Shakes": ["Fruit", "Milk", "Sugar"]
}

requests_per_minute = 5
delay_time = 60 / requests_per_minute

def remove_unprintable_chars(s):
    printable_string = ""
    for c in s:
        if ord(c) < 128 and c.isprintable():
            printable_string += c
        else:
            printable_string += ""  # Replace unprintable character with whitespace
    return printable_string.lstrip().strip()

def filter_printable_strings(strings):
    filtered = []
    for s in strings:
        filtered.append(remove_unprintable_chars(s))
    return filtered

def convert_mg_to_g(amount):
    return amount / 1000

def get_ingredients(item):
    app_id = 'a396278c'
    app_key = 'ca5fb53010beec95f9f51d02515a8a47'
    response = requests.get(f'https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={app_key}&ingr={item}')
    if response.status_code == 200:
        data = response.json()
        if data['hints']:
            for result in data['hints']:
                if "foodContentsLabel" in result['food'] and result['food']['foodContentsLabel'] not in ["", "We are working on getting the ingredients for this item"]:
                    if type(result['food']['foodContentsLabel']) == str:
                        ingredients = result['food']['foodContentsLabel'].split(";")
                        return filter_printable_strings(ingredients)
        return []         
    else:
        return []

def create_restaurant(restaurant_obj):
    with open("menu.csv", newline='') as csvfile:
        menu_item_id = 1
        reader = csv.DictReader(csvfile)

        names = set()
        
        for row in reader:
        
            if "(Large Biscuit)" in row["Item"]:
                row["Item"] = row["Item"].replace("(Large Biscuit)", "").rstrip()
            
            if "(Regular Biscuit)" in row["Item"]:
                row["Item"] = row["Item"].replace("(Regular Biscuit)", "").rstrip()
            
            row["Item"] = remove_unprintable_chars(row["Item"])

            if row["Item"] in names:
                continue

            names.add(row["Item"])
               
            if row["Category"] in ["Beverages", "Coffee & Tea", "Smoothies & Shakes"]:
                if "(Medium)" not in row["Item"]:
                    continue
                else:
                    row["Item"] = row["Item"].replace("(Medium)", "").rstrip()
                    ingredients = drink_ingredients[row["Category"]]
            else:
                ingredients = get_ingredients(row["Item"])
                time.sleep(delay_time)


            if ingredients == []:
                continue
            
            match = re.search(r'(\d+(?:\.\d+)?)\s*(fl\s+)?(oz|g)', row["Serving Size"])

            if match:
                amount = float(match.group(1))
                unit = match.group(3)
                if unit == 'oz':
                    amount *= 28.35 # convert ounces to grams
                
                item_obj = {
                    "item_id" : menu_item_id,
                    "category" : row["Category"],
                    "item_name" : row["Item"],
                    "nutrition_facts" : {
                        "serving_size" : float("{:.1f}".format(amount)),
                        "calories" : float(row["Calories"]),
                        "calories_from_fat": float(row["Calories from Fat"]),
                        "total_fat": float(row["Total Fat"]),
                        "saturated_fat" : float(row["Saturated Fat"]),
                        "trans_fat" : float(row["Trans Fat"]),
                        "cholesterol" : convert_mg_to_g( float(row["Cholesterol"]) ),
                        "sodium" : convert_mg_to_g( float(row["Sodium"]) ),
                        "carbohydrates" : float(row["Carbohydrates"]),
                        "dietary_fiber" : float(row["Dietary Fiber"]),
                        "sugars" : float(row["Sugars"]),
                        "protein": float(row["Protein"])
                    },
                    "ingredients": ingredients
                }
                restaurant_obj["menu_items"].append(item_obj)
                menu_item_id += 1


    with open("restaurants_test.json", "w") as f:
        json.dump(restaurant_obj, f, indent=4)


if __name__ == "__main__":
    restaurant_obj = {
        "restaurant_id" : 1, 
        "restaurant_name" : "McDonald's",
        "address" : "15459 Culver Dr, Irvine, CA 92606",
        "menu_items" : []
        }

    create_restaurant(restaurant_obj)


    