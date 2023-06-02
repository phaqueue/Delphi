import json
from math import sqrt
import requests
import uuid
import sys

nutritionFactList = ["calories", "total_fat", "saturated_fat", "sodium", "carbohydrates",
               "dietary_fiber", "sugars", "protein"]

vegetarianForbidden = ["beef", "pork", "chicken"]
veganForbidden = vegetarianForbidden + ["milk", "egg"]

filterList = ["trans_fat", "cholesterol", "nuts", "spiciness"] + veganForbidden

DRI = {"calories": 2860, "total_fat": 88, "saturated_fat": 0,
               "trans_fat": 0, "cholesterol": 0, "sodium": 1.5, "carbohydrates": 394,
               "dietary_fiber": 38, "sugars": 70, "protein": 62}


total_weight_daily = 1300
totalWeightPerMeal = 500

def safe_str(obj):
    try:
        return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    return ""


class RecommendationSystem:
    def __init__(self):
        self.user = {}
        self.pref = {}
        self.filters = []
        self.items = {}
        self.order = {}
        self.userId = None
        self.restaurantId = None
        self.orderId = None

    def setUserId(self, userId):
        self.userId = userId

    def setRestaurantId(self, restaurantId):
        self.restaurantId = restaurantId

    def setOrderId(self, orderId):
        self.orderId = orderId

    def generateOrder(self, ordered):
        self.orderId = str(self.userId) + 'atRestaurant' + str(self.restaurantId) + '_' + str(uuid.uuid1())
        self.order['restaurantId'] = self.restaurantId
        self.order['orderId'] = self.orderId
        self.order['ordered_items'] = ordered
        self.order['userId'] = self.userId

    def distance(self, A, B):
        total = 0
        for i in range(len(A)):
            total += (A[i] - B[i]) * (A[i] - B[i])
        return sqrt(total)

    def transform(self, nutritionFact, amount, weight):
        nutrient_dri = DRI[nutritionFact]
        if amount == 0:
            return 0
        if nutrient_dri == 0:
            return 5
        nutrient_percentage = amount / nutrient_dri
        weight_percentage = weight / total_weight_daily
        if weight_percentage == nutrient_percentage:
            score = 5
        else:
            score = 5 * (nutrient_percentage / weight_percentage)
        score = min(score, 10)

        return score

    def cmp(self, item):
        A = [value for nutritionFact, value in self.pref.items()]
        B = [
            self.transform(nutritionFact, item['nutritionFacts'][nutritionFact], item['nutritionFacts']['serving_size'])
            for nutritionFact, value in self.pref.items()]
        return self.distance(A, B)

    def removeIneligibles(self):
        for nutritionFact, value in self.pref.items():
            self.items = [item for item in self.items if (nutritionFact in item['nutritionFacts'])]
        for ingredient in self.filters:
            self.items = [item for item in self.items if not (ingredient in item['ingredients'])]

    # output: top K items based on the user's preferences.
    def recommend(self, K):
        # Remove the ineligible food items before recommending
        self.removeIneligibles()

        # Sort the items based on the user preferences
        sortedItems = sorted(self.items, key=self.cmp)

        if (len(sortedItems) < K):
            return sortedItems
        else:
            return sortedItems[0: K]

    # Update the user preference based on the past order
    # We should have the info about user preferences and restaurant now.
    # The update algorithm is intuitive at the moment.
    def update(self):
        totalWeight = 0
        for orderedItem in self.order["ordered_items"]:
            for item in self.items:
                if (orderedItem == item["item_id"]):
                    totalWeight += item["nutritionFacts"]["serving_size"]
                    break
        for nutritionFact in self.pref:
            totalValue = 0
            for orderedItem in self.order["ordered_items"]:
                for item in self.items:
                    if (orderedItem == item["item_id"]):
                        totalValue += item["nutritionFacts"]["serving_size"] * self.transform(nutritionFact,
                                                                                              item["nutritionFacts"][
                                                                                                  nutritionFact],
                                                                                              item["nutritionFacts"][
                                                                                                  "serving_size"])
                        break
            self.pref[nutritionFact] = (self.pref[nutritionFact] + 1.0 * totalValue / totalWeightPerMeal) / (
                        1 + 1.0 * totalWeight / totalWeightPerMeal)

    # Testing API
    def getUserAndRestaurantFromAPI(self):
        user = requests.get(
            'http://ec2-13-57-39-29.us-west-1.compute.amazonaws.com:8080/delphi/users/{}'.format(self.userId)).json()
        restaurant = requests.get(
            'http://ec2-13-57-39-29.us-west-1.compute.amazonaws.com:8080/delphi/restaurants/{}'.format(self.restaurantId)).json()
        self.user = user
        self.pref = user['preferences']
        self.filters = user['filters']
        self.items = restaurant['menu_items']

    def getOrderFromAPI(self):
        self.order = requests.get(
            'http://ec2-13-57-39-29.us-west-1.compute.amazonaws.com:8080/delphi/orders/{}'.format(self.orderId)).json()
    def updatePreference(self):
        # update using API
        url = 'http://ec2-13-57-39-29.us-west-1.compute.amazonaws.com:8080/delphi/users/{}/update'.format(self.userId)
        json_data = json.dumps(self.pref)
        requests.put(url, data=json_data, headers={'Content-Type': 'application/json'})
        user = requests.get(
            'http://ec2-13-57-39-29.us-west-1.compute.amazonaws.com:8080/delphi/users/{}'.format(self.userId)).json()
        self.user = user
        self.pref = user['preferences']
    def sendOrder(self):
        url = 'http://ec2-13-57-39-29.us-west-1.compute.amazonaws.com:8080/delphi/orders/register'
        json_data = json.dumps(self.order)
        requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    def buildFromOrder(self):
        self.userId = self.order['userId']
        self.restaurantId = self.order['restaurantId']
        self.getUserAndRestaurantFromAPI()

if __name__ == "__main__":
    rec = RecommendationSystem()
    args = sys.argv
    rec.setOrderId(args[1])
    rec.getOrderFromAPI()
    rec.buildFromOrder()
    rec.update()
    rec.updatePreference()
    print(safe_str("updated preference: ") + safe_str(rec.pref))


