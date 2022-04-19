from collections import defaultdict
import random


NUM_CUSTOMERS = 200
NUM_ORDERS = 2000
NUM_ORDER_ITEM_CUSTOMIZATIONS = 500


def ingredient():
    columns = ['ingredient_id', 'ingredient_name']
    ingredient_types = ['ketchup',
        'mustard',
        'mayonnaise',
        'lettuce',
        'pickles',
        'onions',
        'tomatoes',
        'cheese',
        'beef',
        'bun',
        'salt',
        'potatoes',
        'coffee',
        'milk',
        'sugar',
        'soda',
        'wheat',
        'ice cream',
        'bacon'
    ]

    ingredients_dict = {}

    with open('CSVs/ingredient.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for id, ingredient in enumerate(ingredient_types):
            file.write(f'{id + 1},{ingredient}\n')
            ingredients_dict[ingredient] = id + 1

    return ingredients_dict


def itemingredient(ingredients_dict):
    columns = ['item_id', 'ingredient_id']
    items = {
        640404923: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes",
        640404963: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes, Beef",
        640405025: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes, Bacon",
        640405058: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes",
        640405085: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes, Beef",
        640405112: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes, Beef",
        640405172: "Ketchup, Mustard, Mayonnaise, Lettuce, Pickles, Onions, Tomatoes, Bacon",
        640405355: "soda",
        640405371: "soda",
        640405380: "soda",
        640405389: "Milk, Ice Cream",
        640405395: "Milk, Ice Cream",
        640405399: "Milk, Ice Cream",
        640405296: "Salt, Potatoes",
        640405307: "Salt, Potatoes",
        640405315: "Salt, Potatoes",
        640405323: "Salt, Potatoes",
        640405331: "Salt, Potatoes",
        640405339: "Salt, Potatoes",
        640405347: "Salt, Onions, Wheat",
        640405348: "Coffee, Milk, Sugar"
    }

    with open('CSVs/itemingredient.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for id, ingredients in items.items():
            ingredient_list = [ingredient.lower() for ingredient in ingredients.split(', ')]

            for ingredient in ingredient_list:
                file.write(f'{id},{ingredients_dict[ingredient]}\n')


def menu():
    columns = ['menu_id', 'item_id', 'brand', 'store_id']
    item_ids = [
        640404923,
        640404963,
        640405025,
        640405058,
        640405085,
        640405112,
        640405172,
        640405355,
        640405371,
        640405380,
        640405389,
        640405395,
        640405399,
        640405296,
        640405307,
        640405315,
        640405323,
        640405331,
        640405339,
        640405347,
        640405348
    ]

    with open('CSVs/menu.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for id, item in enumerate(item_ids):
            file.write(f'{id + 1},{item},"Generic Restaurant",50\n')


def customer():
    columns = ['customer_id', 'opt_in', 'birthday', 'gender']
    genders = [
        'male',
        'female',
        'other'
    ]

    with open('CSVs/customer.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for i in range(1, NUM_CUSTOMERS + 1):
            date = f'{random.randint(1990, 2005)}-{random.randint(1, 12)}-{random.randint(1, 28)}'
            file.write(f'{i},true,{date},{random.choices(genders, weights=[0.45, 0.45, 0.1])[0]}\n')


def order():
    columns = ['order_id', 'customer_id', 'order_timestamp', 'weather']
    weather = [
        'sunny',
        'cloudy',
        'rainy',
        'snowy'
    ]

    random_customer_ids = [random.randint(1, NUM_CUSTOMERS) for i in range(1, NUM_ORDERS + 1)]

    with open('CSVs/order.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for order_id, customer_id in enumerate(random_customer_ids):
            timestamp = f'"{random.randint(2015, 2020)}-{random.randint(1, 12)}-{random.randint(1, 28)} {str(random.randint(0, 23)).zfill(2)}:{str(random.randint(0, 59)).zfill(2)}:{str(random.randint(0, 59)).zfill(2)}"'
            file.write(f'{order_id + 1},{customer_id},{timestamp},{random.choice(weather)}\n')


def orderitem():
    columns = ['order_id', 'item_id']
    item_ids = [
        640404923,
        640404963,
        640405025,
        640405058,
        640405085,
        640405112,
        640405172,
        640405355,
        640405371,
        640405380,
        640405389,
        640405395,
        640405399,
        640405296,
        640405307,
        640405315,
        640405323,
        640405331,
        640405339,
        640405347,
        640405348
    ]

    orders = defaultdict(list)

    with open('CSVs/orderitem.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for id in range(1, NUM_ORDERS + 1):
            item_id = random.choice(item_ids)
            file.write(f'{id},{item_id}\n')
            orders[item_id].append(id)

    return orders


def customization():
    columns = ['customization_id', 'item_id', 'customization']
    customizations = [
        'no ketchup',
        'no mustard',
        'no mayonnaise',
        'no lettuce',
        'no pickles',
        'no onions',
        'no tomatoes'
    ]
    items = [
        640404923,
        640404963,
        640405058,
        640405085,
        640405112
    ]
    bacon_items = [
        640405025,
        640405172
    ]
    no_bacon = 'no bacon'

    customization_dict = defaultdict(list)

    with open('CSVs/customization.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        id = 1
        while True:
            for item in items:
                for customization in customizations:
                    file.write(f'{id},{item},{customization}\n')
                    customization_dict[item].append(id)
                    id += 1

            customizations.append(no_bacon)

            for item in bacon_items:
                for customization in customizations:
                    file.write(f'{id},{item},{customization}\n')
                    customization_dict[item].append(id)
                    id += 1

            break

    return customization_dict


def orderitemcustomization(orders, customization_dict):
    columns = ['order_id', 'item_id', 'customization_id']
    order_item_customizations = set()

    with open('CSVs/orderitemcustomization.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for i in range(NUM_ORDER_ITEM_CUSTOMIZATIONS):
            item_id = random.choice(list(orders.keys()))

            while item_id not in customization_dict:
                item_id = random.choice(list(orders.keys()))

            order_history_id = random.choice(orders[item_id])
            order_item_customizations.add((order_history_id, item_id, random.choice(customization_dict[item_id])))

        for row in order_item_customizations:
            file.write(f'{row[0]},{row[1]},{row[2]}\n')


def dietarypreference():
    columns = ['preference_id', 'preference', 'preference_weight']
    preferences = [
        'dairy',
        'nuts',
        'vegan',
        'vegetarian',
        'kosher',
        'halal'
    ]

    preference_weight_pairs = set()

    for preference in preferences:
        for i in range(1, 6):
            preference_weight_pairs.add((preference, i))

    with open('CSVs/dietarypreference.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for id, pair in enumerate(preference_weight_pairs):
            file.write(f'{id + 1},{pair[0]},{pair[1]}\n')

    return preference_weight_pairs


def customerdietarypreference(preference_weight_pairs):
    columns = ['customer_id', 'preference_id']
    customer_dietary_preference_pairs = set()

    for i in range(1, int(NUM_CUSTOMERS / 4) + 1):
        customer_dietary_preference_pairs.add((random.randint(1, NUM_CUSTOMERS), random.randint(1, len(preference_weight_pairs))))

    with open('CSVs/customerdietarypreference.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for pair in customer_dietary_preference_pairs:
            file.write(f'{pair[0]},{pair[1]}\n')


if __name__ == '__main__':
    ingredients_dict = ingredient()
    itemingredient(ingredients_dict)
    menu()
    customer()
    order()
    orders = orderitem()
    customization_dict = customization()
    orderitemcustomization(orders, customization_dict)
    preference_weight_pairs = dietarypreference()
    customerdietarypreference(preference_weight_pairs)
