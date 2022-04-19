from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

db_username = 'postgres'
db_password = 'postgres'
db_hostname = 'localhost:5432'
db_database = 'delphi'
db_url = f'postgresql+psycopg2://{db_username}:{db_password}@{db_hostname}/{db_database}'

Engine = create_engine(db_url)
Base = declarative_base(metadata = MetaData(bind = Engine))


class Item(Base):
    __table__ = Table('item', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'Item({self.item_id}, {self.item_name}, {self.item_description}, ' + \
               f'{self.item_image}, {self.price}, {self.taste_profile}, {self.item_type})'

    def get_item_id(self):
        return self.item_id

    def get_item_name(self):
        return self.item_name

    def get_item_description(self):
        return self.item_description

    def get_item_image(self):
        return self.item_image

    def get_price(self):
        return self.price

    def get_taste_profile(self):
        return self.taste_profile

    def get_item_type(self):
        return self.item_type


class Ingredient(Base):
    __table__ = Table('ingredient', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'Ingredient({self.ingredient_id}, {self.ingredient_name})'

    def get_ingredient_id(self):
        return self.ingredient_id

    def get_ingredient_name(self):
        return self.ingredient_name


class ItemIngredient(Base):
    __table__ = Table('itemingredient', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'ItemIngredient({self.item_id}, {self.ingredient_id})'

    def get_item_id(self):
        return self.item_id

    def get_ingredient_id(self):
        return self.ingredient_id


class NutritionFacts(Base):
    __table__ = Table('nutritionfacts', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'NutritionFacts({self.nutrition_facts_id}, {self.item_id}, {self.serving_size}, ' + \
               f'{self.calories}, {self.calories_from_fat}, {self.total_fat}, {self.saturated_fat}, ' + \
               f'{self.trans_fat}, {self.cholesterol}, {self.sodium}, {self.total_carbs}, ' + \
               f'{self.dietary_fiber}, {self.total_sugars}, {self.added_sugars}, {self.protein})'

    def get_nutrition_facts_id(self):
        return self.nutrition_facts_id

    def get_item_id(self):
        return self.item_id

    def get_serving_size(self):
        return self.serving_size

    def get_calories(self):
        return self.calories

    def get_calories_from_fat(self):
        return self.calories_from_fat

    def get_total_fat(self):
        return self.total_fat

    def get_saturated_fat(self):
        return self.saturated_fat

    def get_trans_fat(self):
        return self.trans_fat

    def get_cholesterol(self):
        return self.cholesterol

    def get_sodium(self):
        return self.sodium

    def get_total_carbs(self):
        return self.total_carbs

    def get_dietary_fiber(self):
        return self.dietary_fiber

    def get_total_sugars(self):
        return self.total_sugars

    def get_added_sugars(self):
        return self.added_sugars

    def get_protein(self):
        return self.protein


class Menu(Base):
    __table__ = Table('menu', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'Menu({self.menu_id}, {self.item_id}, {self.brand}, {self.store_id})'

    def get_menu_id(self):
        return self.menu_id

    def get_item_id(self):
        return self.item_id

    def get_brand(self):
        return self.brand

    def get_store_id(self):
        return self.store_id


class Customer(Base):
    __table__ = Table('customer', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'Customer({self.customer_id}, {self.opt_in}, {self.birthday}, {self.gender})'

    def get_customer_id(self):
        return self.customer_id

    def get_opt_in(self):
        return self.opt_in

    def get_birthday(self):
        return self.birthday

    def get_gender(self):
        return self.gender


class Order(Base):
    __table__ = Table('order', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'Order({self.order_id}, {self.customer_id}, {self.order_timestamp}, {self.weather})'

    def get_order_id(self):
        return self.order_id

    def get_customer_id(self):
        return self.customer_id

    def get_order_timestamp(self):
        return self.order_timestamp.strftime("%m/%d/%Y %H:%M:%S")

    def get_weather(self):
        return self.weather


class OrderItem(Base):
    __table__ = Table('orderitem', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'OrderItem({self.order_id}, {self.item_id})'

    def get_order_id(self):
        return self.order_id

    def get_item_id(self):
        return self.item_id


class Customization(Base):
    __table__ = Table('customization', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'Customization({self.customization_id}, {self.item_id}, {self.customization})'

    def get_customization_id(self):
        return self.customization_id

    def get_item_id(self):
        return self.item_id

    def get_customization(self):
        return self.customization


class OrderItemCustomization(Base):
    __table__ = Table('orderitemcustomization', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'OrderItemCustomization({self.order_id}, {self.item_id}, {self.customization_id})'

    def get_order_id(self):
        return self.order_id

    def get_item_id(self):
        return self.item_id

    def get_customization_id(self):
        return self.customization_id


class DietaryPreference(Base):
    __table__ = Table('dietarypreference', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'DietaryPreference({self.preference_id}, {self.preference}, {self.preference_weight})'

    def get_preference_id(self):
        return self.preference_id

    def get_preference(self):
        return self.preference

    def get_preference_weight(self):
        return self.preference_weight


class CustomerDietaryPreference(Base):
    __table__ = Table('customerdietarypreference', Base.metadata, autoload = True, schema = 'delphi')

    def __repr__(self):
        return f'CustomerDietaryPreference({self.customer_id}, {self.preference_id})'

    def get_customer_id(self):
        return self.customer_id

    def get_preference_id(self):
        return self.preference_id
