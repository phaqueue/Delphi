-- DROP and recreate the SCHEMA
DROP SCHEMA IF EXISTS delphi CASCADE;
CREATE SCHEMA IF NOT EXISTS delphi;

-- DROP TABLES
DROP TABLE IF EXISTS delphi.CustomerDietaryPreference;
DROP TABLE IF EXISTS delphi.DietaryPreference;
DROP TYPE IF EXISTS delphi.Preference;
DROP TABLE IF EXISTS delphi.OrderItemCustomization;
DROP TYPE IF EXISTS delphi.CustomizationEnum;
DROP TABLE IF EXISTS delphi.Customization;
DROP TABLE IF EXISTS delphi.OrderItem;
DROP TABLE IF EXISTS delphi.Order;
DROP TYPE IF EXISTS delphi.Weather;
DROP TABLE IF EXISTS delphi.Customer;
DROP TYPE IF EXISTS delphi.Gender;
DROP TABLE IF EXISTS delphi.Menu;
DROP TABLE IF EXISTS delphi.NutritionFacts;
DROP TABLE IF EXISTS delphi.ItemIngredient;
DROP TABLE IF EXISTS delphi.Ingredient;
DROP TYPE IF EXISTS delphi.IngredientEnum;
DROP TABLE IF EXISTS delphi.Item;
DROP TYPE IF EXISTS delphi.TasteProfile;
DROP TYPE IF EXISTS delphi.ItemType;

-- CREATE TABLES
CREATE TYPE delphi.ItemType AS ENUM (
    'burger',
    'beverage',
    'side'
);

CREATE TYPE delphi.TasteProfile AS ENUM (
    'savory',
    'healthy',
    'chilling',
    'sweet',
    'bitter'
);

CREATE TABLE delphi.Item (
    item_id int NOT NULL,
    item_name text NOT NULL,
    item_description text,
    item_image text,
    price decimal NOT NULL,
    taste_profile delphi.TasteProfile NOT NULL,
    item_type delphi.ItemType NOT NULL,
    PRIMARY KEY (item_id)
);

CREATE TYPE delphi.IngredientEnum AS ENUM (
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
);

CREATE TABLE delphi.Ingredient (
    ingredient_id int NOT NULL,
    ingredient_name delphi.IngredientEnum NOT NULL,
    PRIMARY KEY (ingredient_id),
    UNIQUE (ingredient_name)
);

-- M:M mapping table for item ingredients
CREATE TABLE delphi.ItemIngredient (
    item_id int NOT NULL,
    ingredient_id int NOT NULL,
    PRIMARY KEY (item_id, ingredient_id),
    FOREIGN KEY (item_id) REFERENCES delphi.Item ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES delphi.Ingredient ON DELETE CASCADE
);

CREATE TABLE delphi.NutritionFacts (
    nutrition_facts_id int NOT NULL,
    item_id int NOT NULL,
    serving_size decimal NOT NULL,
    calories decimal NOT NULL,
    calories_from_fat decimal NOT NULL,
    total_fat decimal NOT NULL,
    saturated_fat decimal NOT NULL,
    trans_fat decimal NOT NULL,
    cholesterol decimal NOT NULL,
    sodium decimal NOT NULL,
    total_carbs decimal NOT NULL,
    dietary_fiber decimal NOT NULL,
    total_sugars decimal NOT NULL,
    added_sugars decimal NOT NULL,
    protein decimal NOT NULL,
    PRIMARY KEY (nutrition_facts_id),
    FOREIGN KEY (item_id) REFERENCES delphi.Item ON DELETE CASCADE
);

CREATE TABLE delphi.Menu (
    menu_id int NOT NULL,
    item_id int NOT NULL,
    brand text NOT NULL,
    store_id int NOT NULL,
    PRIMARY KEY (menu_id),
    FOREIGN KEY (item_id) REFERENCES delphi.Item ON DELETE NO ACTION
);

CREATE TYPE delphi.Gender AS ENUM (
    'male',
    'female',
    'other'
);

CREATE TABLE delphi.Customer (
    customer_id int NOT NULL,
    opt_in boolean NOT NULL,
    birthday date,
    gender delphi.Gender,
    PRIMARY KEY (customer_id)
);

CREATE TYPE delphi.Weather AS ENUM (
    'sunny',
    'cloudy',
    'rainy',
    'snowy'
);

-- Order history for a customer
CREATE TABLE delphi.Order (
    order_id int NOT NULL,
    customer_id int NOT NULL,
    order_timestamp timestamp NOT NULL,
    weather delphi.Weather NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES delphi.Customer ON DELETE CASCADE
);

-- M:M mapping table for ordered items
CREATE TABLE delphi.OrderItem (
    order_id int NOT NULL,
    item_id int NOT NULL,
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES delphi.Order ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES delphi.Item ON DELETE CASCADE
);

CREATE TYPE delphi.CustomizationEnum AS ENUM (
    'no ketchup',
    'no mustard',
    'no mayonnaise',
    'no lettuce',
    'no pickles',
    'no onions',
    'no tomatoes',
    'no bacon'
);

-- Lookup table for all possible item customizations
CREATE TABLE delphi.Customization (
    customization_id int NOT NULL,
    item_id int NOT NULL,
    customization delphi.CustomizationEnum NOT NULL,
    PRIMARY KEY (customization_id),
    UNIQUE (item_id, customization),
    FOREIGN KEY (item_id) REFERENCES delphi.Item ON DELETE CASCADE
);

-- M:M mapping table for order item customizations
CREATE TABLE delphi.OrderItemCustomization (
    order_id int NOT NULL,
    item_id int NOT NULL,
    customization_id int NOT NULL,
    PRIMARY KEY (order_id, item_id, customization_id),
    FOREIGN KEY (order_id, item_id) REFERENCES delphi.OrderItem ON DELETE CASCADE,
    FOREIGN KEY (customization_id) REFERENCES delphi.Customization
);

CREATE TYPE delphi.Preference AS ENUM (
    'dairy-free',
    'nut-free',
    'vegan',
    'vegetarian',
    'kosher',
    'halal'
);

-- Dietary preferences with weights, 1 is can't have, 5 is love
CREATE TABLE delphi.DietaryPreference (
    preference_id int NOT NULL,
    preference delphi.Preference NOT NULL,
    -- preference_weight int NOT NULL,
    PRIMARY KEY (preference_id),
    UNIQUE (preference)
    -- UNIQUE (preference, preference_weight),
    -- CONSTRAINT weight_constraint
    --     CHECK (preference_weight BETWEEN 1 AND 5)
);

-- M:M mapping table for customer dietary preferences
CREATE TABLE delphi.CustomerDietaryPreference (
    customer_id int NOT NULL,
    preference_id int NOT NULL,
    PRIMARY KEY (customer_id, preference_id),
    FOREIGN KEY (customer_id) REFERENCES delphi.Customer,
    FOREIGN KEY (preference_id) REFERENCES delphi.DietaryPreference
);

-- M:M mapping table for item dietary preferences
CREATE TABLE delphi.ItemDietaryPreference (
    item_id int NOT NULL,
    preference_id int NOT NULL,
    PRIMARY kEY (item_id, preference_id),
    FOREIGN KEY (item_id) REFERENCES delphi.Item,
    FOREIGN KEY (preference_id) REFERENCES delphi.DietaryPreference
);
