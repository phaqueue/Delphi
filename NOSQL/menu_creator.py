import json
import csv
import re

def create_restaurant(restaurant_obj):
    with open("menu.csv", newline='') as csvfile:
        menu_item_id = 1
        reader = csv.DictReader(csvfile)
        
        for row in reader:

            if row["Category"] in ["Beverages", "Coffee & Tea", "Smoothies & Shakes"]:
                if "(Medium)" not in row["Item"]:
                    continue
            
            match = re.search(r'(\d+(?:\.\d+)?)\s*(?:(fl\s+)?oz|(g))', row["Serving Size"])

            if match:
                amount = float(match.group(1))
                unit = match.group(2) or "g"
                if unit == 'oz':
                    amount *= 28.35 # convert ounces to grams

                item_obj = {
                    "item_id" : menu_item_id,
                    "category" : row["Category"],
                    "item_name" : row["Item"],
                    "nutrition_facts" : {
                        "serving_size" : f"{amount:.1f} g",
                        "calories" : float(row["Calories"]),
                        "calories_from_fat": float(row["Calories from Fat"]),
                        "total_fat": float(row["Total Fat"]),
                        "saturated_fat" : float(row["Saturated Fat"]),
                        "trans_fat" : float(row["Trans Fat"]),
                        "cholesterol" : float(row["Cholesterol"]),
                        "sodium" : float(row["Sodium"]),
                        "carbohydrates" : float(row["Carbohydrates"]),
                        "dietary_fiber" : float(row["Dietary Fiber"]),
                        "sugars" : float(row["Sugars"]),
                        "protein": float(row["Protein"])
                    }
                }

                restaurant_obj["menu_items"].append(item_obj)

                menu_item_id += 1


    with open("restaurants.json", "w") as f:
        json.dump(restaurant_obj, f, indent=4)


if __name__ == "__main__":
    restaurant_obj = {
        "restaurant_id" : 1, 
        "restaurant_name" : "McDonald's",
        "address" : "15459 Culver Dr, Irvine, CA 92606",
        "menu_items" : []
        }

    create_restaurant(restaurant_obj)


    