# Recommendation System Explained

“Most executives in multinational corporations are thoughtlessly accommodating. They falsely presume that marketing means giving customers what they say they want rather than trying to understand exactly what they would like.” -- Theodore Levitt, *The Globalization of Markets*

This system contains two parts:
  1. Recommend food items based on the menu and the user preferences
  2. Update the user preferences based on users' orders

But before I go over these two parts, let's examine the important elements in *restaurant.JSON*, *user.JSON*, and *order.JSON*. I will show some examples of these JSON files at the end.

## restaurant.JSON
  The most important parts are *nutrition_facts* and *ingredients* inside the object *menu_items*.
  1. ***nutrition_facts***.
    It is an Object that contains all of the nutrition facts (in grams) that we think are important plus the weight of the food item (we call it *serving_size*). For example, *total_fat* for an *Egg McMuffin* is *13*. It means that there are 13 grams of fat in the entire Egg McMuffin. The devs may add more facts in the future.
  2. ***ingredients***.
    It is an array that contains all of the ingredients used for the food item. If an ingredient is not inside the array, we assume the food item must not contain this ingredient.

## user.JSON
  1. ***preferences***.
    It is similar to the *nutrition_facts* in *restaurant.JSON*, except the values are from 0 ~ 10, which denotes how much a user likes those nutrients. If the value is 0, it means the user does not want the nutrient in their food; if the value is 5, it means the user is indifferent to it; if the value is 10, it means the user would like food items that have as much this nutrient as possible. For example, if the value for *sugar* is *10*, they would like food whose density of sugar is approaching infinity. They will prefer a 100g soda (let's use *g* instead of *ml* for convenience) with 90g sugar than a 100g soda with 85g sugar. Note that there is no difference between a 100g soda with 90g sugar and a 1000g soda with 900g sugar, as the density of sugar is the same.
  2. ***filters***.
    It is similar to the *ingredients* in *restaurant.JSON*. If an ingredient is in the array, it means that the user cannot have food with this particular ingredient (because of allergies or religious beliefs or else)

## order.JSON
  ***ordered_items***.
    It is an array that contains all of the ids of items ordered by a user at a restaurant (drive-thru) in a transaction. For example, if the array is *\[1, 1, 2, 3\]*, it means the user ordered a food item, whose id is 1, twice, and also food item 2 and food item 3.
    
Now let's check the two parts of the recommendation system.

## Recommend
  It takes restaurant.JSON, user.JSON, and *K* as input, and outputs the top K items that match the user's preferences most. Here are the main steps.
  1. Remove the ineligible food items. These items include those whose nutrition facts are missing some nutrients (because they are outdated) and those which have ingredients the user cannot have, according to the user's *filters*.
  2. Turn the nutrition facts of the food items into a value from 0 ~ 10, in order to match the user's preferences. Currently, to convert the value for a nutrient, we take "the amount of this nutrient", "the weight of the food item", "the Dietary Reference Intakes of this nutrient", and "the weight of food an average person eats". For example, the weight of Big Mac is 200g, the fat it contains is 27g, and we know one should take around 90g of fat daily, and one is expected to eat 1500g (these numbers may be inaccurate, but the inaccuracy should not affect the accuracy of results much, as we are mainly comparing different food items) of food daily. Thus, the ratio of nutrient_percentage and weight_percentage is ((27 / 90) / (200 / 1500)) = 2.25, meaning that the fat in the burger would be 2.25 times more than the "healthy and balanced food" recommended. And the new value we assign will be 10 * (2.25 / (1 + 2.25)) = 6.92. Note if the ratio is 1 instead, the value would be 5, which is the value for indifference.
  3. Rank the food items based on their similarities with the user's preferences, and return the top K items. We originally were thinking of using Cosine Similarity, but later I realized that using Euclidean Distance makes more sense. If the distance between two vectors is small, it is likely this food item will be recommended.

## Update
  It takes restaurant.JSON, user.JSON, and order.JSON as input, and outputs an updated user.JSON (because the user's preferences are updated based on the order).
  1. We combine all of the food items into a hodgepodge item for convenience, and transform the nutrition facts (refer to bullet point 2 of ***Recommend***). Suppose the weight of this item is w_item.
  2. We also consider how much an average person eats per meal. Let's call it w_meal.
  3. For each nutrition fact, suppose the original value of the user's preference of that nutrient is v_user, and the value of the hodgepodge item for that is v_item. The new value would be (v_user + v_item / (w_total / w_meal)) / (1 + w_total / w_meal). The more the user buys, the larger weight this order has (it has more influence) when updating the user's preference. Currently if the user buys exactly average meal, the formula will be simplified to (v_user + v_item) / 2. But no matters how much the user buys, the new value will always be a value between v_user and v_item.

I'm aware that the recommendation system may not be perfect, but I hope it is reasonable. And the algorithm will eventually be replaced by machine learning after enough data is gathered, so tuning my algorithm should not be the main focus of the project.
