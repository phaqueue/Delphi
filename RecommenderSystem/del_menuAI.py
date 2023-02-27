import psycopg2
import numpy as np

"""
    This file will contain our recommedner system which will retrive a user_id and user preferences as an array
    of weights given a bluetooth id. Given a menu id we will compute top N ranking menu items using cosine 
    similarity between user preference array and menu item "feature array" 
    Our system will use collaborative-filtering algorithm
    - Model notes can be found here https://docs.google.com/document/d/17sQhlbMRWL60sXNzwtVgcGfjcryh2b2Lt-RIgvFFO7s/edit
    - Our repository can be found here https://github.com/phaqueue/Delphi
"""

conn = psycopg2.connect(
    dbname="delphi",
    user="postgres",
    password="Strike30",
    host="localhost",
    port="5432"
)


def cosine_similarity(user_arr, item_arr):
    """
        Computes cosine similarity between a user preference array and a menu item feature array
    """
    dot_product = np.dot(user_arr, item_arr)
    norm_a = np.linalg.norm(user_arr)
    norm_b = np.linalg.norm(item_arr)
    return dot_product / (norm_a * norm_b)
    

def obtain_user(bluetooth_id):
    """
    Given a bluetooth id should connect to database and retrieve and return user_id
    """
    return None

def recommend_items(user_id, menu_id):
    """
    Overall Recommendation algorithm that given a user id we would retrieve user preferences and build the "feature"
    vector.
    Given menu_id we retrieve all menu items in that menu and form a item "feature" vector
    we can compute similarity between user and items and recommend the N highest scoring items.
    """
    item_amount_to_rec = 8
    return None


if __name__ == "__main__":
    """
    This file should be run whenever the drive thru's BLE Sensor obtains a bluetooth id should be passed as a 
    command line argument
    """
    pass
