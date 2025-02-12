CREATE SCHEMA Delphi;
DROP TABLE IF EXISTS Delphi.users;
DROP TABLE IF EXISTS Delphi.restaurants;
DROP TABLE IF EXISTS Delphi.menus;
DROP TABLE IF EXISTS Delphi.food_items;
DROP TABLE IF EXISTS Delphi.nutrition_facts;

CREATE TABLE Delphi.users (
	user_id int UNIQUE NOT NULL, --or bluetooth_id to be precise
	phone_number int UNIQUE, -- a web app cannot detect the bluetooth_id, so maybe having phone number in the primary key can make things easier
	gender varchar(30),
	first_name varchar(30),
	last_name varchar(30),
	birthday date,
	
	PRIMARY KEY (user_id)
);

CREATE TABLE Delphi.restaurants (
	restaurant_id int UNIQUE NOT NULL,
	name varchar(30),
	
	PRIMARY KEY (restaurant_id)
);

-- We don't need to store an ordered menu
CREATE TABLE Delphi.menus (
	restaurant_id int UNIQUE NOT NULL,
	menu_id int UNIQUE NOT NULL,
	name varchar(30),
	
	PRIMARY KEY (restaurant_id, menu_id),
	FOREIGN KEY (restaurant_id) REFERENCES Delphi.restaurants(restaurant_id) ON DELETE CASCADE
);

CREATE TABLE Delphi.food_items (
	menu_id int UNIQUE NOT NULL,
	item_id int UNIQUE NOT NULL,
	
	PRIMARY KEY (menu_id, item_id),
	FOREIGN KEY (menu_id) REFERENCES Delphi.menus(menu_id) ON DELETE CASCADE
);

CREATE TABLE Delphi.nutrition_facts (
	
	--one of the user_id or item_id has a value while the other one is NULL,
	--indicating it is an user preference or item nutrition facts
	nutrition_id int UNIQUE NOT NULL,
	user_id int,
	item_id int,
	
	--The below nutrition facts are rated from 0 to 10, from cannot have to must have (user preferences)
	--or from does not contain to has huge amount of them (item nutrition facts).
	cholestrol real,
	sodium real,
	protein real,
	added_sugar real,
	total_sugar real,
	dietary_fiber real,
	total_carbs real,
	total_fat real,
	saturated_fat real,
	trans_fat real,
	calories real,
	--We can potentially add more.
	
	--Are the foreign keys correct?
	PRIMARY KEY (user_id, item_id, nutrition_id),
	FOREIGN KEY (user_id) REFERENCES Delphi.users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (item_id) REFERENCES Delphi.food_items(item_id) ON DELETE CASCADE
);
