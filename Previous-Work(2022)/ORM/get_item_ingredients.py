import csv

from sqlalchemy import func, cast, String
from sqlalchemy.orm import create_session
from sqlalchemy.sql.elements import literal_column
import delphi

def run():
    session = create_session(bind = delphi.Engine)

    query = session.query(delphi.Item.item_id, func.string_agg(cast(delphi.Ingredient.ingredient_name, String), literal_column("', '"))) \
                   .join(delphi.ItemIngredient, delphi.Item.item_id == delphi.ItemIngredient.item_id) \
                   .join(delphi.Ingredient, delphi.ItemIngredient.ingredient_id == delphi.Ingredient.ingredient_id) \
                   .group_by(delphi.Item.item_id)

    columns = ['item_id', 'has_ketchup', 'has_mustard', 'has_mayonnaise', 'has_lettuce', 'has_pickles', 'has_onions', \
               'has_tomatoes', 'has_cheese', 'has_beef', 'has_bun', 'has_salt', 'has_potatoes', 'has_coffee', \
               'has_milk', 'has_sugar', 'has_soda', 'has_wheat', 'has_ice_cream', 'has_bacon']
    rows = []

    for row in query:
        ingredients = row[1].split(', ')
        new_row = [
            row[0],
            True if 'ketchup' in ingredients else False,
            True if 'mustard' in ingredients else False,
            True if 'mayonnaise' in ingredients else False,
            True if 'lettuce' in ingredients else False,
            True if 'pickles' in ingredients else False,
            True if 'onions' in ingredients else False,
            True if 'tomatoes' in ingredients else False,
            True if 'cheese' in ingredients else False,
            True if 'beef' in ingredients else False,
            True if 'bun' in ingredients else False,
            True if 'salt' in ingredients else False,
            True if 'potatoes' in ingredients else False,
            True if 'coffee' in ingredients else False,
            True if 'milk' in ingredients else False,
            True if 'sugar' in ingredients else False,
            True if 'soda' in ingredients else False,
            True if 'wheat' in ingredients else False,
            True if 'ice cream' in ingredients else False,
            True if 'bacon' in ingredients else False
        ]

        rows.append(new_row)

    with open('CSVs/item_ingredients.csv', 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(columns)
        csvwriter.writerows(rows)

    # SELECT 
    #     it.item_id, string_agg(CAST(ing.ingredient_name AS varchar), ', ') 
    # FROM 
    #     delphi.Item it, delphi.ItemIngredient ii, delphi.Ingredient ing
    # WHERE 
    #     it.item_id = ii.item_id AND ii.ingredient_id = ing.ingredient_id 
    # GROUP BY 
    #     it.item_id;

if __name__ == '__main__':
    run()
