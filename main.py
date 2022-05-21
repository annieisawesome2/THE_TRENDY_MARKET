'''
Title: The trendy market
Author: Annie Sun
Date: 2022-05-18
'''
#from selectitems import selectMeat, selectDairy, selectFrozen, selectFruits, selectVegetables, selectCondiments, selectBaking
import pathlib
import sqlite3
 
## --- VARIABLES --- ##
MARKET = "the_trendy_market.csv"
DATABASE_FILE = "market.db"
 
FIRST_RUN = True
 
# Test if FILENAME already exists
if (pathlib.Path.cwd() / DATABASE_FILE).exists():
   FIRST_RUN = False
 
CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = CONNECTION.cursor()
 
##--INPUTS--##
def menu():
   """User selects program actions
 
   returns(int): CHOICE
   """
   print('''
Please choose an option
   1. Shop for Groceries
   2. Cart/Checkout
   3. Shop Manager
   ''')
   CHOICE = input("> ")
   CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
   if CHOICE > 0 and CHOICE < 4:
       return CHOICE
   else:
       print("Please choose a valid number from the menu selection!")
       return menu()
 
def checkInt(NUMBER): ## sourced from Calc2.py
   """Verifies the number is an integer
 
   Args:
       NUMBER (string):
 
   Returns:
       (int): The numeric equivalent
   """
   if NUMBER.isnumeric():
       return int(NUMBER)
   else:
       print("That is not a number!")
       NEW_NUM = input("Please enter a valid number: ")
       return checkInt(NEW_NUM)

def getInput(QUESTION, ANSWER): 
   """verifies inputted answer is valid
 
   Args:
       QUESTION (str):
       ANSWER (str):
 
   Returns:
       str: returns a capitalized answer if answer is valid
   """
   INPUT = input(f"{QUESTION}: ") #makes sure the user inputs specific things in square brackets later on the the inputs
   if INPUT.title() in ANSWER:
       return INPUT.title()## capitalizes user's input
   else:
       print("Sorry, the item you are looking for is not available in this category of trendy foods.")
       return getInput(QUESTION, ANSWER)


def shopSections():
    """Where user can choose what section to shop in

    Returns:
        _type_: _description_
    """
    print('''
What section would you like to shop in?
    1. Meats
    2. Dairy
    3. Frozen
    4. Fruits
    5. Vegetables
    6. Condiments
    7. Baking
    ''')
    CHOICE = input("> ")
    CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
    if CHOICE > 0 and CHOICE < 8:
        return CHOICE
    else:
        print("Please choose a valid number from the selection provided!!")
        return shopSections()
    
def sortCategory(CATEGORY):
    for i in range(len(CATEGORY)):
        print(f"- {CATEGORY[i][2]} (${CATEGORY[i][3]})")



def selectMeat():
    ITEM = getInput("Please type in the item you would like to view from the meat products listed", ["Ground Beef", "Maple Roast Beef", "Beef Tenderloin Steak", "Striploin Grilling Steak", "Steak Shoulder Blade", "Ham", "Sirloin Steak", "Pork Tenderloin Whole", "Pork Side Ribs", "Ground Pork Lean", "Pork Sausage", "Bacon", "Pork Chops Loin", "Pork Bellies", "Turkey Hind Quarter", "Turkey Pepperoni", "Turkey Ground Thigh", "Turkey Breast", "Hot Italian Sausage", "Pork Sausages", "Chicken Breast Boneless", "Chicken Thighs", "Chicken Drumsticks", "Chicken Whole"])                                                                 
    return ITEM

def selectDairy():
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Skim Milk", "1% Milk", "2% Milk", "3% Milk", "Whipping Cream", "Chocolate Milk", "Parmesan Cheese", "Cheddar Cheese", "Swiss Cheese", "Strawberry Yogurt", "Blueberry Yogurt", "Vanilla Yogurt", "Greek Yogurt", "White Eggs", "Brown Eggs", "Sour Cream", "Butter", "Feta Cheese", "Almond Milk", "Cashew Milk"])
    return ITEM

def selectFrozen():
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Vanilla Ice Cream", "Chocolate Ice Cream", "Strawberry Ice Cream", "Orange Popsicles", "Frozen Blueberries", "Frozen Strawberries", "Frozen Rasberries", "Frozen Mangoes", "Frozen Pinapples", "Frozen Blackberries", "Frozen Scallops", "Frozen Peas", "Frozen Fillets", "Frozen Prawns", "Frozen Salmon"])
    return ITEM

def selectFruits():
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Blueberries", "Pinapple","Strawberries","Bananas","Apples","Oranges","Mandarins","Peaches","Green Grapes","Red Grapes","Mangoes","Dragon Fruit","Passion Fruit","Watermelon","Pears","Cherries"])
    return ITEM

def selectVegetables():
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Mushrooms","Red Onions","Garlic","Avacados","Green Peppers","Celery","Carrot","Potatoes","Tomatoes","Cucumbers","Lettuce","Cabbage","Green Onions","Romaine Hearts","Peas","Red peppers","Yellow Peppers","Orange Peppers","Zucchini","Kale","Winter Melon","Beets","Corn","Yam","Spinach","Baby Spinach","Broccoli","Squash","Green Bean","Cilantro","Ginger","Turnip","Pumpkin"])
    return ITEM

def selectCondiments():
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Mustard","Ketchup","Relish","Mayo","Ranch","Honey","Sriracha","Soy Sauce","Olive Oil","Canola Oil","Mayonnaise","Maple Syrup","Hot Sauce","Vinager"])
    return ITEM

def selectBaking():
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Sugar","Salt","Flour","Coca Powder","Baking Powder","Baking Soda","Vanilla Cake Mix","Chocolate Cake Mix","Icing","Butter Cream","Classic Sprinkles","Vanilla Extract","Blue Food Coloring","Yellow Food Coloring","Red Food Coloring","Pink Food Coloring","Green Food Coloring","Icing Sugar","Baking Soda","Chocolate Chips","Almond Extract","Cinnamon","Brown Sugar","Yeast","Red Velvet Cake Mix","Whole Wheat Flour","Cornmeal","Cornstarch"])
    return ITEM

def directionChoice():
    print('''
    1. Add item to Cart
    2. Continue Shopping
    3. Checkout

    ''')
    CHOICE = input("> ")
    CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
    if CHOICE > 0 and CHOICE < 4:
       return CHOICE
    else:
       print("Please choose a valid number from the menu selection!")
       return menu()

def askQuantity():
    ##must check if quantity is less than what is available
    pass

##--PROCESSING--##
def getRawData(MARKET):
   """Read CSV file and extract unprocessed data
 
   Args:
       FILENAME (str):
   Returns
       (list): 2D array of data
   """
   FILE = open(MARKET)
   CONTENT = FILE.readlines() #puts in array
   FILE.close()
   TOTAL_DATA = []
 
   ## checking for and ignoring any commas in comments
   for DATA in CONTENT:
 
       DATA = DATA.rstrip() #removes the \n at the end of each line
       LIST = []
       start = False
       end = False
       checks = ""
 
 
       #checking for a normal value in list to proceed with appending the value separated by commas into an array
       for i in range(len(DATA)):
     
           checks = checks + DATA[i]
 
           if DATA[i] == "," and start == False:
               LIST.append(checks[:-1])
               checks = ""
           #checking if there is a comment so we can keep the comma within the comment but don't recognize it as a split
           elif DATA[i] == '"' and start == False:
               checks = ""
               start = True
     
           elif DATA[i] == '"' and start == True: #if a character is "
               if i == len(DATA) - 1:
                   LIST.append(checks[:-1])
     
               end = True
     
           elif DATA[i] == "," and end == True: #checks if comma is between ""
               LIST.append(checks[:-2])
               checks = ""
               end = False
               start = False
         
           elif i == len(DATA)-1:
               LIST.append(checks)
     
       TOTAL_DATA.append(LIST)
   return TOTAL_DATA

def setup():
   """Create Database tables
   """
   global CURSOR, CONNECTION
 
   #CREATE MARKET TABLE
   CURSOR.execute('''
       CREATE TABLE
           market (
               id PRIMARY KEY,
               category TEXT,
               item,
               price,
               description,
               quantity
                   )
   ;''')
   CONNECTION.commit()   


def importData(RAW_DATA):
   """load and import data
 
   Args:
       RAW_DATA (list): 2D array
 
   """
   global CURSOR, CONNECTION
 

   ## making sure data is null in database if array value is empty or NA. 
   ## turning numeric values in data to become integers
   for i in range(len(RAW_DATA)):
       RAW_DATA[i][0] = int(RAW_DATA[i][0])
       RAW_DATA[i][3] = float(RAW_DATA[i][3])
       RAW_DATA[i][5] = int(RAW_DATA[i][5])
        
        
           
       CURSOR.execute('''
           INSERT INTO
               market
           VALUES(
               ?, ?, ?, ?, ?, ?
           )  
       ;''', RAW_DATA[i])

   CONNECTION.commit()


def shopMeats():
    global CURSOR
    MEATS = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Meat"
     
    ;''').fetchall()
    return MEATS

def shopDairy():
    global CURSOR
    DAIRY = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Dairy"
     
    ;''').fetchall()
    return DAIRY

def shopFrozen():
    global CURSOR
    FROZEN = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Frozen"
     
    ;''').fetchall()

    return FROZEN

def shopFruits():
    global CURSOR
    FRUITS = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Fruits"
     
    ;''').fetchall()
    return FRUITS


def shopVegetables():
    global CURSOR
    VEGETABLES = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Vegetables"
     
    ;''').fetchall()
    return VEGETABLES


def shopCondiments():
    global CURSOR
    CONDIMENTS = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Condiments"
     
    ;''').fetchall()

    return CONDIMENTS

def shopBaking():
    global CURSOR
    BAKING = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            category = "Baking"
     
    ;''').fetchall()

    return BAKING

def getProduct(ITEM):
    global CURSOR
    PRODUCT = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            item = ?
    ;''', [ITEM]).fetchone()

    print(PRODUCT)

    return PRODUCT

##--OUTPUTS--##
def intro():
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Trendy Market!! We source the best quality foods from this planet!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

def displayProducts(PRODUCT):
        print(f'''
{PRODUCT[2]}
----------------------
{PRODUCT[4]}

Price: ${PRODUCT[3]}
Quantity Available: {PRODUCT[5]}

        ''')

if __name__ == "__main__":
    if FIRST_RUN:
        setup()
        RAW_DATA = getRawData(MARKET)
        importData(RAW_DATA)

    intro()
    while True:
        OPERATION = menu()

        if OPERATION == 1:
            CATEGORY = shopSections()

            if CATEGORY == 1:
                MEATS = shopMeats()
                sortCategory(MEATS)
                MEAT_ITEM = selectMeat()
                PRODUCT = getProduct(MEAT_ITEM) #array with product details
                
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()


                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass
                
            elif CATEGORY == 2:
                DAIRY = shopDairy()
                sortCategory(DAIRY)
                DAIRY_ITEM = selectDairy()
                PRODUCT = getProduct(DAIRY_ITEM)
                DIRECTION = directionChoice()

                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass

            elif CATEGORY == 3:
                FROZEN = shopFrozen()
                sortCategory(FROZEN)
                FROZEN_ITEM= selectFrozen()
                PRODUCT = getProduct(FROZEN_ITEM)
                DIRECTION = directionChoice()

                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass

            elif CATEGORY == 4:
                FRUITS = shopFruits()
                sortCategory(FRUITS)
                FRUIT_ITEM = selectFruits()
                PRODUCT = getProduct(FRUIT_ITEM)
                DIRECTION = directionChoice()

                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass

            elif CATEGORY == 5:
                VEGETABLES = shopVegetables()
                sortCategory(VEGETABLES)
                VEG_ITEM = selectVegetables()
                PRODUCT = getProduct(VEG_ITEM)
                DIRECTION = directionChoice()

                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass
                
            elif CATEGORY == 6:
                CONDIMENTS = shopCondiments()
                sortCategory(CONDIMENTS)
                CONDIMENT_ITEM = selectCondiments()
                PRODUCT = getProduct(CONDIMENT_ITEM)
                DIRECTION = directionChoice()

                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass
                 
            elif CATEGORY == 7:
                BAKING =shopBaking()
                sortCategory(BAKING)
                BAKING_ITEM = selectBaking()
                PRODUCT = getProduct(BAKING_ITEM)
                DIRECTION = directionChoice()

                if DIRECTION == 1:
                        pass
                if DIRECTION == 2:
                        pass
                if DIRECTION == 3:
                        pass

        if OPERATION == 2:
            pass

        if OPERATION == 3:
            pass

