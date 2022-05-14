from collections import defaultdict
import random

NUM_CUSTOMERS = 200
NUM_ORDERS = 2000
NUM_ORDER_ITEM_CUSTOMIZATIONS = 500


def ingredient():
    '''Populates ingredient.csv with ingredient_id and ingredient_name 
    given the ingredient_types declared here. Returns csv content as dict().'''

    columns = ['ingredient_id', 'ingredient_name']
    ingredient_types = [
        'ketchup',
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
    ingredients_dict = dict()

    with open('CSVs/ingredient.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        # Create lookup table: ingredient_id, ingredient_name
        for id, ingredient in enumerate(ingredient_types):
            file.write(f'{id + 1},{ingredient}\n')
            ingredients_dict[ingredient] = id + 1

    # ingredient: ingredient_id
    return ingredients_dict


def itemingredient(ingredients_dict):
    '''Populates itemingredient.csv with item_id and ingredient_id 
    given the ingredients for each item.'''

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

            # Create mapping table: item_id, ingredient_id
            for ingredient in ingredient_list:
                file.write(f'{id},{ingredients_dict[ingredient]}\n')


def menu():
    '''Currently assigns menu_id to each item_id with all the
    same restaurant brand and store_id. (i.e. All items belong
    to the same store.) Populates menu.csv.'''

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

        # Create menu table: menu_id, item_id, brand, store_id
        for id, item in enumerate(item_ids):
            file.write(f'{id + 1},{item},"Generic Restaurant",50\n')


def customer():
    '''Generates {NUM_CUSTOMERS} customers with random attributes except
    everyone has opt_in = true because we have this information only for
    opt_in folks as of now. Populates customer.csv.'''

    columns = ['customer_id', 'opt_in', 'birthday', 'gender']
    genders = [
        'male',
        'female',
        'other'
    ]

    with open('CSVs/customer.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        # Create customer: customer_id, opt_in, birthday (randomly chosen), gender (randomly chosen, weighted more heavily towards male or female)
        for i in range(1, NUM_CUSTOMERS + 1):
            date = f'{random.randint(1990, 2005)}-{random.randint(1, 12)}-{random.randint(1, 28)}'
            file.write(f'{i},true,{date},{random.choices(genders, weights=[0.45, 0.45, 0.1])[0]}\n')


def order():
    '''Generates {NUM_ORDERS} orders with order_id, a random customer_id,
    a random timestamp between 2015 and 2020, and weather chosen from a list.'''

    columns = ['order_id', 'customer_id', 'order_timestamp', 'weather']
    weather = [
        'sunny',
        'cloudy',
        'rainy',
        'snowy'
    ]
    customer_orders = defaultdict(list)
    random_customer_ids = [random.randint(1, NUM_CUSTOMERS) for i in range(1, NUM_ORDERS + 1)]

    with open('CSVs/order.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        # Create order: order_id, customer_id (randomly chosen), order_timestamp (randomly chosen), weather (randomly chosen)
        for order_id, customer_id in enumerate(random_customer_ids):
            timestamp = f'"{random.randint(2015, 2020)}-{random.randint(1, 12)}-{random.randint(1, 28)} {str(random.randint(0, 23)).zfill(2)}:{str(random.randint(0, 59)).zfill(2)}:{str(random.randint(0, 59)).zfill(2)}"'
            customer_orders[customer_id].append(order_id + 1)
            file.write(f'{order_id + 1},{customer_id},{timestamp},{random.choice(weather)}\n')

    # customer_id: [order_id]
    return customer_orders


def orderitem(customer_orders, customer_preferences, item_preferences):
    '''Creates a random orderitem that suits the preferences.'''

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

        # Loop through all order ids
        for id in range(1, NUM_ORDERS + 1):
            valid_items = [item for item in item_ids]
            items = set()
            num_items = random.randint(1, 4)

            # Loop through customer orders
            for customer, order in customer_orders.items():
                # If id is in customer order list
                if id in order:
                    customer_preference_ids = customer_preferences[customer]

                    # Loop through item restrictions
                    for item, preference in item_preferences.items():
                        # If customer has preferences, check if they match the item
                        for preference_id in customer_preference_ids:
                            # If the customer preference not in item preference, remove the item
                            if preference_id not in preference and item in valid_items:
                                valid_items.remove(item)

            if valid_items:
                # Choose random items
                for i in range(num_items):
                    items.add(random.choice(valid_items))

                # Create orderitem: order_id, item_id
                for item in items:
                    file.write(f'{id},{item}\n')
                    orders[item].append(id)

    # item_id: [order_id]
    return orders


def customization():
    '''Menu items with customizable features (ingredients that
    can be taken out) propagate customization.csv which each
    menu item - customization pair. (E.g. burger_type1 with no ketchup
    could be a row and burger_type1 with no mustard could be another.'''

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

    # Create lookup table for all possible item customizations
    with open('CSVs/customization.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        id = 1
        while True:
            # For every item, create a customization if it can be customized
            for item in items:
                for customization in customizations:
                    file.write(f'{id},{item},{customization}\n')
                    customization_dict[item].append(id)
                    id += 1

            customizations.append(no_bacon)

            # For the items with bacon, add the 'no bacon' customization
            for item in bacon_items:
                for customization in customizations:
                    file.write(f'{id},{item},{customization}\n')
                    customization_dict[item].append(id)
                    id += 1

            break

    # item_id: [customization_id]
    return customization_dict


def orderitemcustomization(orders, customization_dict):
    '''Pairs {NUM_ORDER_ITEM_CUSTOMIZATIONS} random orders with customizations
    where the item_id matches.'''
    columns = ['order_id', 'item_id', 'customization_id']
    order_item_customizations = set()

    with open('CSVs/orderitemcustomization.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        # For number of order item customizations, randomly choose and item and order and customize it
        for i in range(NUM_ORDER_ITEM_CUSTOMIZATIONS):
            item_id = random.choice(list(orders.keys()))

            while item_id not in customization_dict:
                item_id = random.choice(list(orders.keys()))

            order_id = random.choice(orders[item_id])
            order_item_customizations.add((order_id, item_id, random.choice(customization_dict[item_id])))

        # Create orderitemcustomization: order_id, item_id, customization_id
        for row in order_item_customizations:
            file.write(f'{row[0]},{row[1]},{row[2]}\n')


def dietarypreference():
    # Code for weighted preferences
    # columns = ['preference_id', 'preference', 'preference_weight']
    columns = ['preference_id', 'preference']
    preferences = [
        'dairy-free',
        'nut-free',
        'vegan',
        'vegetarian',
        'kosher',
        'halal'
    ]
    preference_ids = dict()

    # Code for weighted preferences
    # preference_weight_pairs = set()

    # for preference in preferences:
    #     for i in range(1, 6):
    #         preference_weight_pairs.add((preference, i))

    with open('CSVs/dietarypreference.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        # Code for weighted preferences
        # for id, pair in enumerate(preference_weight_pairs):
        #     file.write(f'{id + 1},{pair[0]},{pair[1]}\n')

        # Create lookup table for every preference: preference_id, preference
        for id, preference in enumerate(preferences):
            file.write(f'{id + 1},{preference}\n')
            preference_ids[preference] = id + 1

    # preference: preference_id
    return preference_ids


def customerdietarypreference(preference_ids):
    '''Every few customers will have a preference attached to them.'''

    columns = ['customer_id', 'preference_id']
    preference_list = list(preference_ids.values())
    customer_preferences = defaultdict(list)

    with open('CSVs/customerdietarypreference.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        for customer_id in range(1, NUM_CUSTOMERS + 1):
            # Random weighted choice for how many preferences a customer has (0-5)
            num_preferences = random.choices((range(len(preference_ids))), weights=(50,35,10,2,2,1))[0]

            if num_preferences > 0:
                preferences = random.sample(preference_list, num_preferences)

                # Create customerdietarypreference: customer_id, preference_id (randomly chosen)
                for preference_id in preferences:
                    customer_preferences[customer_id].append(preference_id)
                    file.write(f'{customer_id},{preference_id}\n')

    # customer_id: [preference_id]
    return customer_preferences


def itemdietarypreference(preference_ids):
    columns = ['item_id', 'preference_id']
    item_restrictions = {
        640404923: 'dairy-free,nut-free,halal,kosher',
        640404963: 'nut-free,halal',
        640405025: 'nut-free',
        640405058: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405085: 'dairy-free,nut-free,halal,kosher',
        640405112: 'nut-free,halal',
        640405172: 'nut-free',
        640405355: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405371: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405380: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405389: 'nut-free,vegetarian,halal,kosher',
        640405395: 'nut-free,vegetarian,halal,kosher',
        640405399: 'nut-free,vegetarian,halal,kosher',
        640405296: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405307: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405315: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405323: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405331: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405339: 'dairy-free,nut-free,vegan,vegetarian,halal,kosher',
        640405347: 'nut-free,vegetarian,halal,kosher',
        640405348: 'nut-free,vegetarian,halal,kosher'
    }
    item_preferences = defaultdict(list)

    with open('CSVs/itemdietarypreference.csv', 'w') as file:
        file.write(','.join(columns) + '\n')

        # Create restriction list from dictionary
        for item_id, restrictions in item_restrictions.items():
            restriction_list = [restriction.lower() for restriction in restrictions.split(',')]

            # Create lookup table: item_id, preference_id
            for restriction in restriction_list:
                item_preferences[item_id].append(preference_ids[restriction])
                file.write(f'{item_id},{preference_ids[restriction]}\n')

    # item_id: [preference_id]
    return item_preferences



if __name__ == '__main__':
    ingredients_dict = ingredient()
    itemingredient(ingredients_dict)
    menu()
    customer()

    preference_ids = dietarypreference()
    customer_preferences = customerdietarypreference(preference_ids)
    item_preferences = itemdietarypreference(preference_ids)

    customer_orders = order()
    orders = orderitem(customer_orders, customer_preferences, item_preferences)
    customization_dict = customization()
    orderitemcustomization(orders, customization_dict)
