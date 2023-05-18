# Recommendation System Explained

“Most executives in multinational corporations are thoughtlessly accommodating. They falsely presume that marketing means giving customers what they say they want rather than trying to understand exactly what they would like.” -- Theodore Levitt, *The Globalization of Markets*

This system contains two parts:
  1. Recommend food items based on the menu and the user preferences
  2. Update the user preferences based on users' orders

But before I go over these two parts, let's examine the important elements in *restaurant.JSON*, *user.JSON*, and *order.JSON*. I will show some examples of these JSON files at the end.

## restaurant.JSON
  The most important parts are *nutrition_facts* and *ingredients* inside the object *menu_items*.
  1. nutrition_facts
    It is an Object that contains all of the nutrition facts (in grams) that we think are important plus the weight of the food item (we call it *serving_size*). For example, *total_fat* for an *Egg McMuffin* is *13*. It means that there are 13 grams of fat in the entire Egg McMuffin. The devs may add more facts in the future.
  2. ingredients
    It is an array that contains all of the ingredients used for the food item. If an ingredient is not inside the array, we assume the food item must not contain this ingredient.

## user.JSON
  1. preferences
    It is similar to the *nutrition_facts* in *restaurant.JSON*, except the values are from 0 ~ 10, which denotes how much a user likes those nutrients. If the value is 0, it means the user does not want the nutrient in their food; if the value is 5, it means the user is indifferent to it; if the value is 10, it means the user would like food items that have as much this nutrient as possible. For example, if the value for *sugar* is *10*, they would like food whose density of sugar is approaching infinity. They will prefer a 100g soda (let's use *g* instead of *ml* for convenience) with 90g sugar than a 100g soda with 85g sugar. Note that there is no difference between a 100g soda with 90g sugar and a 1000g soda with 900g sugar, as the density of sugar is the same.
  2. filters
    It is similar to the *ingredients* in *restaurant.JSON*. If an ingredient is in the array, it means that the user cannot have food with this particular ingredient (because of allergies or religious beliefs or else)


I'm aware that my recommendation system may not be perfect, but I hope it is reasonable. And the algorithm will eventually be replaced by machine learning after enough data is gathered, so tuning my algorithm should not be the main focus of the project.
