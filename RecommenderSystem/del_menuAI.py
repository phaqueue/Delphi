import psycopg2
import numpy as np
import sys

"""
    This file will contain our recommeder system which will retrive a user_id and user preferences as an array
    of weights given a bluetooth id. Given a menu id we will compute top N ranking menu items using cosine 
    similarity between user preference array and menu item "feature array" 
    Our system will use collaborative-filtering algorithm
    - Model notes can be found here https://docs.google.com/document/d/17sQhlbMRWL60sXNzwtVgcGfjcryh2b2Lt-RIgvFFO7s/edit
    - Our repository can be found here https://github.com/phaqueue/Delphi
"""

def obtain_user_id(bluetooth_id, conn):
    """
    Given a bluetooth id should connect to database and retrieve and return user_id
    """
    user_id = None
    cur = conn.cursor() 
    return user_id

def obtain_user_weights(user_id, conn):
    """
    Based on our final schema the function should retrieve
    user preference weigths based on user_id
    """
    return []

def obtain_user_filters(user_id, conn):
    """
    Based on our final schema the function should retrieve
    user preference filters based on user_id
        - Filters can be whehther person is vegan, lactose, etc.
        - I was thinking using some sort of tag system in a item entry 
    This is a work in progress as it's some sort of idea for addtions in terms of our final item
    recommedations
    """
    return []

def obtain_items(menu_id, conn, user_filters=None):
    """
    This function should return a list of item_ids and if we give user_filters
    then it should filter out the items that do not satisfy the user given constraints
    """
    return []

def cosine_similarity(user_arr, item_arr):
    """
        Computes cosine similarity between a user preference array and a menu item feature array
    """
    dot_product = np.dot(user_arr, item_arr)
    norm_a = np.linalg.norm(user_arr)
    norm_b = np.linalg.norm(item_arr)
    return dot_product / (norm_a * norm_b)

def recommend_items(user_weights, user_filters, menu_id, conn):
    """
    Overall Recommendation algorithm that given user weights & possibly user filters
    recommend intems given a menu/restaurant id
    Given menu_id we retrieve all menu items in that menu and form a item "feature" vector for each item
    we can compute similarity between user and items and recommend the N highest scoring items.

    - Should return a list of top N items
    """
    item_amount_to_rec = 8
    return []

def begin_recommending(args, conn):
    # obtain command line arguments
    user_bluetooth_id = args[1]
    #restaurant_id = args[2]
    menu_id = args[2]

    # obtain user_id first using bluetooth_id
    user_id = obtain_user_id(user_bluetooth_id, conn)

    # after obtaining user_id obtain preference weights and item filters

    user_weights = obtain_user_weights(user_id, conn)
    user_filters = obtain_user_filters(user_id, conn)

    # once retrieved arrays begin recommend items based on restaurant id or menu id

    items_recommended = recommend_items(user_weights, user_filters, menu_id, conn)

    print(f"Items Recommended for you: {items_recommended}\n")

if __name__ == "__main__":
    """
    This file could be run be run whenever the drive thru's BLE Sensor obtains a bluetooth id should be passed as a 
    command line argument

    - Addition (How to know what menu to use?), for now we will assume that our application will know the either
    restaurant or menu id to retrieve which items to recommend
    """
    if len(sys.argv) != 2:
        """
        ERROR in providing command line args
        """
        sys.exit(1)

    conn = psycopg2.connect(
        dbname="delphi",
        user="postgres",
        password="Strike30",
        host="localhost",
        port="5432")
    
    begin_recommending(sys.argv, conn)

    # done recommending close connection
    conn.close()       
