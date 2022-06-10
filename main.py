'''
Title: The trendy market
Author: Annie Sun
Date: 2022-05-18
'''

import pathlib
import sqlite3

 
## --- VARIABLES --- ##
MARKET = "the_trendy_market.csv"

ACCOUNTS = "accounts.db"
DATABASE_FILE = "market.db"

FIRST_RUN = True

ITEM = [0, "", 0, 0] #price, product, quantity, points
CART = []
# Test if FILENAME already exists
if (pathlib.Path.cwd() / DATABASE_FILE).exists():
   FIRST_RUN = False
 
CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = CONNECTION.cursor()

ACCOUNT_CON = sqlite3.connect(ACCOUNTS)
ACCOUNT_CUR = ACCOUNT_CON.cursor()

#### ------INPUTS ------ ####
def menu():
   """User selects program actions
 
   returns(int): CHOICE
   """
   print('''
Please choose an option
   1. Shop for Groceries
   2. Cart/Checkout
   3. Shop Manager
   4. Exit
   ''')
   CHOICE = input("> ")
   CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
   if CHOICE > 0 and CHOICE < 5:
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

def inputFoods(QUESTION, ANSWER): 
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
       print("Sorry, the item you are looking for is not available in The Trendy Market.")
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
    


def selectMeat():
    """User can select a meat product

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the meat products listed", ["Ground Beef", "Maple Roast Beef", "Beef Tenderloin Steak", "Striploin Grilling Steak", "Steak Shoulder Blade", "Ham", "Sirloin Steak", "Pork Tenderloin Whole", "Pork Side Ribs", "Ground Pork Lean", "Pork Sausage", "Bacon", "Pork Chops Loin", "Pork Bellies", "Turkey Hind Quarter", "Turkey Pepperoni", "Turkey Ground Thigh", "Turkey Breast", "Hot Italian Sausage Meat", "Pork Sausages", "Chicken Breast Boneless", "Chicken Thighs", "Chicken Drumsticks", "Chicken Whole"])                                                                 
    return ITEM

def selectDairy():
    """User can select a dairy product

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the dairy products listed", ["Skim Milk", "1% Milk", "2% Milk", "3% Milk", "Whipping Cream", "Chocolate Milk", "Parmesan Cheese", "Cheddar Cheese", "Swiss Cheese", "Strawberry Yogurt", "Blueberry Yogurt", "Vanilla Yogurt", "Greek Yogurt", "White Eggs", "Brown Eggs", "Sour Cream", "Butter", "Feta Cheese", "Almond Milk", "Cashew Milk"])
    return ITEM

def selectFrozen():
    """User can select a frozen product

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the frozen products listed", ["Vanilla Ice Cream", "Chocolate Ice Cream", "Strawberry Ice Cream", "Popsicles", "Frozen Blueberries", "Frozen Strawberries", "Frozen Rasberries", "Frozen Mangoes", "Frozen Pineapples", "Frozen Blackberries", "Frozen Scallops", "Frozen Peas", "Frozen Fillets", "Frozen Prawns", "Frozen Salmon"])
    return ITEM

def selectFruits():
    """User can select a fruit product

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the fruit products listed", ["Blueberries", "Pineapple","Strawberries","Bananas","Apples","Oranges","Mandarins","Peaches","Green Grapes","Red Grapes","Mangoes","Dragon Fruit","Passion Fruit","Watermelon","Pears","Cherries"])
    return ITEM

def selectVegetables():
    """User can select a vegetable product

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the vegetable products listed", ["Mushrooms","Red Onions","Garlic","Avacados","Green Peppers","Celery","Carrot","Potatoes","Tomatoes","Cucumbers","Lettuce","Cabbage","Green Onions","Romaine Hearts","Peas","Red peppers","Yellow Peppers","Orange Peppers","Zucchini","Kale","Winter Melon","Beets","Corn","Yam","Spinach","Baby Spinach","Broccoli","Squash","Green Bean","Cilantro","Ginger","Turnip","Pumpkin"])
    return ITEM

def selectCondiments():
    """User can select a condiment

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the condiment products listed", ["Mustard","Ketchup","Relish","Peanut Butter","Ranch","Honey","Sriracha","Soy Sauce","Olive Oil","Canola Oil","Mayonnaise","Maple Syrup","Hot Sauce","Vinager"])
    return ITEM

def selectBaking():
    """User can select a baking product

    Returns:
       str: 
    """
    ITEM = getInput("Please type in the item you would like to view from the baking products listed", ["Sugar","Salt","Flour","Cocoa Powder","Baking Powder","Baking Soda","Vanilla Cake Mix","Chocolate Cake Mix","Icing","Almond Flour","Classic Sprinkles","Vanilla Extract","Blue Food Coloring","Yellow Food Coloring","Red Food Coloring","Pink Food Coloring","Green Food Coloring","Icing Sugar","Nutmeg","Chocolate Chips","Almond Extract","Cinnamon","Brown Sugar","Yeast","Red Velvet Cake Mix","Whole Wheat Flour","Cornmeal","Cornstarch"])
    return ITEM

def directionChoice():
    """User can choose to add item to cart, continue shopping, or go back to main menu

    Returns:
        _type_: _description_
    """
    print('''
    1. Add item to Cart
    2. Continue Shopping
    3. Main menu

    ''')
    CHOICE = input("> ")
    CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
    if CHOICE > 0 and CHOICE < 4:
       return CHOICE
    else:
       print("Please choose a valid number from the menu selection!")
       return directionChoice()

def askQuantity(PRODUCT):
    """Input quantity and check availability of stock

    Args:
        PRODUCT (list): 

    Returns:
        int: quantity
    """
    
    QUANTITY = input("Quantity? ")
    QUANTITY = checkInt(QUANTITY)

    AVAILABLE = PRODUCT[5]
    
    ##must check if quantity is less than what is available
    if QUANTITY > AVAILABLE:
        print("There is not enough in stock. Please enter a new quantity.")
        return askQuantity(PRODUCT)
    else:
        return QUANTITY
            

def askCheckOut(): ## sourced from Calc2.py
    """Asking to continue
    """
    AGAIN = input("Purchase items? (Y/n)")
    return AGAIN

def review(ITEM):
    """user can input a review

    Args:
        ITEM (str): product

    Returns:
        str: review
    """
    REVIEW = input(f"Write your review for {ITEM}: ")
    REVIEW = f'"{REVIEW}",'
    return REVIEW

def getAnyInput(QUESTION):
    """checks for a correct input

    Args:
        QUESTION (str): 

    Returns:
        str: 
    """
    INPUT = input(f"Please enter {QUESTION}: ")
    if INPUT == "":
        print("Cannot be left blank")
        return getAnyInput(QUESTION)
    else:
        return INPUT


def manageMenu():
   """User selects program action in shop manager section
 
   returns(int): 
   """
   print('''
Please choose an option
   1. View customer transaction
   2. Update product quantity/stock
   3. Back to main menu
   ''')
   CHOICE = input("> ")
   CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
   if CHOICE > 0 and CHOICE < 4:
       return CHOICE
   else:
       print("Please choose a valid number from the menu selection!")
       return menu()

def getAccount():
    """getting user's account to view their past transactions

    Returns:
        str: 
    """
    global ACCOUNT_CUR
    ACCOUNT_USERNAME = input("Please enter the account username you would like to view: ")

    if  " " in ACCOUNT_USERNAME:
        print("Please enter a valid username with no spaces or special characters!")
        return getAccount()
    
    elif ACCOUNT_USERNAME.isalnum() == False:
        print("Please enter a valid username with no spaces or special characters!")
        return getAccount()

       
    else:
        ##if valid input is entered: 
        try:
            CUSTOMER = ACCOUNT_CUR.execute(f'''
                SELECT
                    *
                FROM 
                    {ACCOUNT_USERNAME}
    
                ;''').fetchall()
            
        except sqlite3.OperationalError:
            print("Sorry, the username you provided does not exist.")
            return getAccount()
        
        return CUSTOMER, ACCOUNT_USERNAME
            
    
def manageStock():
    """updating stock from market
    """
    global CURSOR, CONNECTION
    
    ASK_ITEM = inputFoods("Please enter the item to update", ["Ground Beef", "Maple Roast Beef", "Beef Tenderloin Steak", "Striploin Grilling Steak", "Steak Shoulder Blade", "Ham", "Sirloin Steak", "Pork Tenderloin Whole", "Pork Side Ribs", "Ground Pork Lean", "Pork Sausage", "Bacon", "Pork Chops Loin", "Pork Bellies", "Turkey Hind Quarter", "Turkey Pepperoni", "Turkey Ground Thigh", "Turkey Breast", "Hot Italian Sausage Meat", "Pork Sausages", "Chicken Breast Boneless", "Chicken Thighs", "Chicken Drumsticks", "Chicken Whole", "Skim Milk", "1% Milk", "2% Milk", "3% Milk", "Whipping Cream", "Chocolate Milk", "Parmesan Cheese", "Cheddar Cheese", "Swiss Cheese", "Strawberry Yogurt", "Blueberry Yogurt", "Vanilla Yogurt", "Greek Yogurt", "White Eggs", "Brown Eggs", "Sour Cream", "Butter", "Feta Cheese", "Almond Milk", "Cashew Milk", "Vanilla Ice Cream", "Chocolate Ice Cream", "Strawberry Ice Cream", "Popsicles", "Frozen Blueberries", "Frozen Strawberries", "Frozen Rasberries", "Frozen Mangoes", "Frozen Pineapples", "Frozen Blackberries", "Frozen Scallops", "Frozen Peas", "Frozen Fillets", "Frozen Prawns", "Frozen Salmon", "Blueberries", "Pineapple","Strawberries","Bananas","Apples","Oranges","Mandarins","Peaches","Green Grapes","Red Grapes","Mangoes","Dragon Fruit","Passion Fruit","Watermelon","Pears","Cherries", "Mushrooms","Red Onions","Garlic","Avacados","Green Peppers","Celery","Carrot","Potatoes","Tomatoes","Cucumbers","Lettuce","Cabbage","Green Onions","Romaine Hearts","Peas","Red peppers","Yellow Peppers","Orange Peppers","Zucchini","Kale","Winter Melon","Beets","Corn","Yam","Spinach","Baby Spinach","Broccoli","Squash","Green Bean","Cilantro","Ginger","Turnip","Pumpkin", "Mustard","Ketchup","Relish","Peanut Butter","Ranch","Honey","Sriracha","Soy Sauce","Olive Oil","Canola Oil","Mayonnaise","Maple Syrup","Hot Sauce","Vinager", "Sugar","Salt","Flour","Cocoa Powder","Baking Powder","Baking Soda","Vanilla Cake Mix","Chocolate Cake Mix","Icing","Almond Flour","Classic Sprinkles","Vanilla Extract","Blue Food Coloring","Yellow Food Coloring","Red Food Coloring","Pink Food Coloring","Green Food Coloring","Icing Sugar","Nutmeg","Chocolate Chips","Almond Extract","Cinnamon","Brown Sugar","Yeast","Red Velvet Cake Mix","Whole Wheat Flour","Cornmeal","Cornstarch"])                                                                 
    ITEM = ASK_ITEM.title()
    
    CHOICE = input("New Quantity: ")
    CHOICE = checkInt(CHOICE) ##checking if inputted answer is an integer
    
    CURSOR.execute('''
        UPDATE
            market
        SET
            quantity = ?
        WHERE
            item = ?
    ;''', [CHOICE, ITEM])

    CONNECTION.commit()

    print(f"{ITEM} quantity has been updated to {CHOICE} available")

#### ------ PROCESSING ------ ####
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
               quantity, 
               review, 
               points
                   )
   ;''')
   CONNECTION.commit()   


def importData(RAW_DATA):
   """load and import data
 
   Args:
       RAW_DATA (list): 2D array
 
   """
   global CURSOR, CONNECTION
 
   RAW_DATA.pop(0)

   ## making sure data is null in database if array value is empty or NA. 
   ## turning numeric values in data to become integers
   
   for i in range(len(RAW_DATA)):
       RAW_DATA[i][0] = int(RAW_DATA[i][0])
       RAW_DATA[i][3] = float(RAW_DATA[i][3])
       RAW_DATA[i][5] = int(RAW_DATA[i][5])
       RAW_DATA[i][7] = int(RAW_DATA[i][7])

   for i in range(len(RAW_DATA)):
       for j in range(len(RAW_DATA[i])):
           if RAW_DATA[i][j] == ("" or "NA"):
               RAW_DATA[i][j] = None
          
       CURSOR.execute('''
           INSERT INTO
               market
           VALUES(
               ?, ?, ?, ?, ?, ?, ?, ?
           )  
       ;''', RAW_DATA[i])

   CONNECTION.commit()


def shopMeats():
    """getting meats from database

    Returns:
        list: 
    """
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
    """getting dairy products from database

    Returns:
        list: 
    """
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
    """getting frozen products from database

    Returns:
        list: 
    """
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
    """getting fruits from database

    Returns:
        list: 
    """
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
    """getting vegetables from database

    Returns:
        list: 
    """
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
    """getting condiments from database

    Returns:
        list: 
    """
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
    """getting baking products from database

    Returns:
        list: 
    """
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
    """getting single array with info for chosen product

    Args:
        ITEM (str): 

    Returns:
        list: 
    """
    global CURSOR
    PRODUCT = CURSOR.execute('''
        SELECT
            *
        FROM 
            market
        WHERE
            item = ?
    ;''', [ITEM]).fetchone()

    return PRODUCT

def itemTotal(PRODUCT, QUANTITY):
    """multiplying item price by quantity

    Args:
        PRODUCT (list): 
        QUANTITY (int): 

    Returns:
        int:
    """
    TOTAL_FOR_ITEM = PRODUCT[3] * QUANTITY
    return TOTAL_FOR_ITEM

def item(ITEM_TOTAL, MEAT_ITEM, QUANTITY, POINTS):
    """putting all items from market database into a list

    Args:
        ITEM_TOTAL (flaot): 
        MEAT_ITEM (str): 
        QUANTITY (int): 
        POINTS (int): 

    Returns:
        list: 
    """
    ITEM[0] = ITEM_TOTAL
    ITEM[1] = MEAT_ITEM
    ITEM[2] = QUANTITY
    ITEM[3] = POINTS
    return ITEM

def cart(ITEM, CART):
    """appending to cart array

    Args:
        ITEM (list): 
        CART (list): 

    Returns:
        _type_: _description_
    """
    CART.append(ITEM[:])
    return CART

def updateQuantity(CART):
    """update quantity of item in database

    Args:
        CART (list): 
    """
    global CURSOR, CONNECTION
    for i in range(len(CART)):

        ## getting the initial quantity
        INITIAL_QUANTITY = CURSOR.execute('''
            SELECT
                *
            FROM
                market
            WHERE
                item = ?
        ;''', [CART[i][1]]).fetchone()

        UPDATED_QUANTITY = INITIAL_QUANTITY[5] - CART[i][2]


        CURSOR.execute('''
            UPDATE
                market
            SET
                quantity = ?
            WHERE
                item = ?
        
        
        ;''', [UPDATED_QUANTITY, CART[i][1]])

        CONNECTION.commit()
        
        

def purchased(CART):
    """reviewing items and putting reviews into database

    Args:
        CART (list):
    """
    global CURSOR, CONNECTION

    ADD = input("Give a review? Y/n")

    if ADD == "N" or ADD == "n":
        for i in range(len(CART)):
            CART.clear()
    

    else:
        for i in range(len(CART)):
            print(f"{i+1}. {CART[i][1]}")

        while True:
            CHOICE = input("Pleace input the corresponding number: ")
            CHOICE = checkInt(CHOICE)
            if CHOICE < 1 or CHOICE > len(CART):
                print("Please enter a valid input")
            else:
                break
        
        ITEM_CHOICE = CART[CHOICE-1][1]
        REVIEW = review(ITEM_CHOICE)

        PAST_REVIEWS = CURSOR.execute('''
            SELECT 
                *
            FROM
                market
            WHERE
                item = ?
        ;''', [ITEM_CHOICE]).fetchone()

        PAST_REVIEWS = PAST_REVIEWS[-2]

        if PAST_REVIEWS == None:
            PAST_REVIEWS = ""

        NEW_REVIEWS = PAST_REVIEWS + REVIEW

        CURSOR.execute('''
            UPDATE
                market
            SET
                review = ?
            WHERE
                item = ?
        ;''', [NEW_REVIEWS, ITEM_CHOICE])

        CONNECTION.commit()
        print("Your review has been saved!")

        CART.pop(CHOICE-1)

        if len(CART) == 0:
            CART = []
            return

        return purchased(CART)


def totalCost():
    """Total the cost and points that may be earned from the transaction

    Returns:
       float: 
    """
    TOTAL = 0
    COUNT_POINTS = 0
    for i in range(len(CART)):
        POINTS = CART[i][3]
        QUANTITY = CART[i][2]
        POINTS_FINAL = POINTS * QUANTITY
        CART_MONEY = CART[i][0]
        COUNT_POINTS += POINTS_FINAL
        TOTAL += CART_MONEY

    TOTAL = round(TOTAL, 2)
    TOTAL = "{:.2f}".format(TOTAL)
    print(f'''
Total cost: ${TOTAL}''')
    print(f"You can earn {COUNT_POINTS} points from this cart!")
    print("Each point is worth $0.02 at The Trendy Market! Buy more = Save more")
    return TOTAL


def customerAccountManagement(TOTAL_COST):
    """creating account, inputting data into account, using existing account, using points from account

    Args:
        TOTAL_COST (float):

    """
    global ACCOUNT_CUR, ACCOUNT_CON

    ### -- CREATING NEW ACCOUNT --- ###
    ASK_ACCOUNT = input("Do you have an existing account with The Trendy Market?(Y/n) ")
    if ASK_ACCOUNT == "n" or ASK_ACCOUNT == "N" or ASK_ACCOUNT == "no" or ASK_ACCOUNT == "No":

        ACCOUNT_USERNAME =  getAnyInput("a username with no spaces or special characters")


        ##check for spaces or special characters
        if  " " in ACCOUNT_USERNAME:
            print("Please enter a valid username with no spaces or special characters!")
            return customerAccountManagement(TOTAL_COST)
        
        elif ACCOUNT_USERNAME.isalnum() == False:
            print("Please enter a valid username with no spaces or special characters!")
            return customerAccountManagement(TOTAL_COST)

        #if all is good, proceed with trying to create a table
        else:
            try:
                ACCOUNT_CUR.execute(f'''
                    CREATE TABLE 
                        {ACCOUNT_USERNAME} (
                            points INTEGER, 
                            product TEXT, 
                            quantity INTEGER,
                            total_price 
                    )
                ;''')

                ACCOUNT_CON.commit()

            #checking if username is taken. If taken, return to ask if they have an account.
            except sqlite3.OperationalError: 
                print("sorry this username is taken. Please enter a new one. ")
                return customerAccountManagement(TOTAL_COST)

        #if all goes well with creating a table, proceed with inserting cart items into user's database
        for i in range(len(CART)):
                PRICE = CART[i][0]
                PRODUCT = CART[i][1]
                QUANTITY = CART[i][2]
                POINTS = CART[i][3]
                
                ACCOUNT_CUR.execute(f'''
                    INSERT INTO 
                        {ACCOUNT_USERNAME}(
                            points, 
                            product, 
                            quantity,
                            total_price 
                        )
                    VALUES (
                        ?, ?, ?, ?
                        )
                    
                        ;''',[POINTS, PRODUCT, QUANTITY, PRICE])

                ACCOUNT_CON.commit()      
  
    ### -- USING EXISTING ACCOUNT --- ###
    else:
        USERNAME = input("Please enter you username: ")

        ##checking for spaces or special characters
        if  " " in USERNAME:
            print("Please enter a valid username with no spaces or special characters!")
            return customerAccountManagement(TOTAL_COST)
        
        elif USERNAME.isalnum() == False:
            print("Please enter a valid username with no spaces or special characters!")
            return customerAccountManagement(TOTAL_COST)

       
        else:
            ##if valid input is entered: 
            try:
                ##get points from existing account
                POINTS = ACCOUNT_CUR.execute(f'''
                            SELECT
                                *
                            FROM
                                {USERNAME}
                        ;''').fetchall()
                
                #get total points including quantity
                TOTAL = 0
                for i in range(len(POINTS)):
                    VALUES_POINTS = POINTS[i][0]
                    QUANTITY = POINTS[i][2]
                    TOTAL_POINTS = QUANTITY * VALUES_POINTS
                    TOTAL += TOTAL_POINTS
                MONEY = TOTAL * 0.02
                MONEY = "{:.2f}".format(MONEY)

                print(f'''
You have a total of {TOTAL} points!
This corresponds to ${MONEY} usable at The Trendy Market!
            ''')

                ##spending the points
                SPEND = input("Would you like to use your points for this purchase?(Y/n) ")
                if  SPEND == "y" or  SPEND == "Y" or  SPEND == "yes" or  SPEND == "Yes":
                    ##set points to zero for past items if user chooses to spend
                    ACCOUNT_CUR.execute(f'''
                        UPDATE
                            {USERNAME}
                        SET
                            points = 0
                        ;''')

                    ACCOUNT_CON.commit()


                    TOTAL_COST = float(TOTAL_COST)
                    MONEY = float(MONEY)

                    NEW_COST = TOTAL_COST - MONEY
                    NEW_COST = "{:.2f}".format(NEW_COST)
                    print(f"Your new total at The Trendy Market is ${NEW_COST}")

                #if user doesn't want to use the point, don't go through the database at all
                else:
                    pass
            
            ##if username does not exist. 
            except sqlite3.OperationalError:
                print("Sorry, the username you provided does not exist. Please create a new account if you do not have a valid existing username.")
                return customerAccountManagement(TOTAL_COST)
            

            #after existing points are used, continue to insert newly purchased items into the cart    
            for i in range(len(CART)):
                PRICE = CART[i][0]
                PRODUCT = CART[i][1]
                QUANTITY = CART[i][2]
                POINTS = CART[i][3]
                
                try:
                    ACCOUNT_CUR.execute(f'''
                        INSERT INTO 
                            {USERNAME}(
                                points, 
                                product, 
                                quantity,
                                total_price 
                            )
                        VALUES (
                            ?, ?, ?, ?
                            )
                        
                            ;''',[POINTS, PRODUCT, QUANTITY, PRICE])

                    ACCOUNT_CON.commit()


                except sqlite3.OperationalError:
                    print("Sorry, the username you provided does not exist. Please create a new account if you do not have a valid existing username.")
                    return customerAccountManagement(TOTAL_COST)

            

def getPoints(PRODUCT):
    """getting the points from product 1D array

    Args:
        PRODUCT (str): 

    Returns:
        int: points
    """
    global CURSOR
    POINTS_ARRAY = CURSOR.execute('''
        SELECT
            *
        FROM
            market
        WHERE 
            item = ?
    ;''', [PRODUCT]).fetchone()
    
    POINTS = POINTS_ARRAY[7]
    
    return POINTS
    

#### ------ OUTPUTS ------ ####
def intro():
    """starting screen
    """
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Trendy Market!! We source the best quality foods from this planet!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

def sortCategory(CATEGORY):
    """displaying all items of a certain category

    Args:
        CATEGORY (): 
    """
    for i in range(len(CATEGORY)):
        print(f"- {CATEGORY[i][2]} (${CATEGORY[i][3]})")


def displayProducts(PRODUCT):
    """displaying the product information from array

    Args:
        PRODUCT (list):
    """

    RAW_DATA = CURSOR.execute('''
        SELECT
            *
        FROM
            market
        WHERE
            item = ?
    ;''', [PRODUCT[2]]).fetchone()

    DATA = RAW_DATA[-2]
    LIST = []
    start = False
    end = False
    checks = ""
    TOTAL_DATA = []

    if DATA != None:
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

    print(f'''
{PRODUCT[2]}
----------------------
{PRODUCT[4]}

Price: ${PRODUCT[3]}
Quantity Available: {PRODUCT[5]}

Reviews:''')

    if DATA != None:
        REVIEWS = TOTAL_DATA[0]

        for review in REVIEWS:
            print("~", review)
    else:
        print("There are no reviews")

def displayCart(CART):
    """displaying the cart with quantity and prices

    Args:
        CART (list):
    """
    for i in range(len(CART)):
        UNIT_PRICE = CART[i][0]
        ITEM = CART[i][1]
        QUANTITY = CART[i][2]
        UNIT_PRICE = "{:.2f}".format(UNIT_PRICE)

    
        print(f"{ITEM}(x{QUANTITY}) = ${UNIT_PRICE}")

def addedToCart():
    """displaying message that item has been added to cart
    """
    for i in range(len(CART)):
        PRODUCT = CART[i][1]
        QUANTITY = CART[i][2]

    print(f'''
{PRODUCT}(x{QUANTITY}) is successfully added to cart!
        ''')

def displayCustomerHistory(ACCOUNT, ACCOUNT_USERNAME):
    """displaying customers past transactions

    Args:
        ACCOUNT (_type_): _description_
        ACCOUNT_USERNAME (_type_): _description_
    """
    print(f'''
{ACCOUNT_USERNAME}
~~~~~~~~~~~~~~~~~~
    ''')
    TOTAL = 0
    for i in range(len(ACCOUNT)):
        PRODUCT = ACCOUNT[i][1]
        QUANTITY = ACCOUNT[i][2]
        COST =  ACCOUNT[i][3]
        VALUES_POINTS = ACCOUNT[i][0]
        TOTAL_POINTS = QUANTITY * VALUES_POINTS
        TOTAL += TOTAL_POINTS
        COST = "{:.2f}".format(COST)
        print(f"{PRODUCT} (x{QUANTITY}) = {COST}")
    MONEY = TOTAL * 0.02
    MONEY = "{:.2f}".format(MONEY)
    print(f"Total points usable for next purchase: {TOTAL} (${MONEY})")



######## -------- MAIN PROGRAM -------- ########
if __name__ == "__main__":
    if FIRST_RUN:
        setup()
        RAW_DATA = getRawData(MARKET)
        importData(RAW_DATA)

    intro()
    while True:

        OPERATION = menu()

        while OPERATION == 1:
            CATEGORY = shopSections()

            if CATEGORY == 1:##meats
                MEATS = shopMeats()
                sortCategory(MEATS)
                MEAT_ITEM = selectMeat()
                PRODUCT = getProduct(MEAT_ITEM) #array with product details
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()

                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(MEAT_ITEM)
                    ITEM = item(ITEM_TOTAL, MEAT_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break
                
                
            elif CATEGORY == 2:##dairy
                DAIRY = shopDairy()
                sortCategory(DAIRY)
                DAIRY_ITEM = selectDairy()
                PRODUCT = getProduct(DAIRY_ITEM)
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()


                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(DAIRY_ITEM)
                    ITEM = item(ITEM_TOTAL, DAIRY_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break

            elif CATEGORY == 3:##frozen
                FROZEN = shopFrozen()
                sortCategory(FROZEN)
                FROZEN_ITEM = selectFrozen()
                PRODUCT = getProduct(FROZEN_ITEM)
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()

                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(FROZEN_ITEM)
                    ITEM = item(ITEM_TOTAL, FROZEN_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break

            elif CATEGORY == 4:##fruits
                FRUITS = shopFruits()
                sortCategory(FRUITS)
                FRUIT_ITEM = selectFruits()
                PRODUCT = getProduct(FRUIT_ITEM)
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()

                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(FRUIT_ITEM)
                    ITEM = item(ITEM_TOTAL, FRUIT_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break

            elif CATEGORY == 5:##vegetables
                VEGETABLES = shopVegetables()
                sortCategory(VEGETABLES)
                VEG_ITEM = selectVegetables()
                PRODUCT = getProduct(VEG_ITEM)
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()

                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(VEG_ITEM)
                    ITEM = item(ITEM_TOTAL, VEG_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break
                
            elif CATEGORY == 6:##condiments
                CONDIMENTS = shopCondiments()
                sortCategory(CONDIMENTS)
                CONDIMENT_ITEM = selectCondiments()
                PRODUCT = getProduct(CONDIMENT_ITEM)
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()

                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(CONDIMENT_ITEM)
                    ITEM = item(ITEM_TOTAL, CONDIMENT_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break
                
            elif CATEGORY == 7:##baking
                BAKING = shopBaking()
                sortCategory(BAKING)
                BAKING_ITEM = selectBaking()
                PRODUCT = getProduct(BAKING_ITEM)
                displayProducts(PRODUCT)

                DIRECTION = directionChoice()

                if DIRECTION == 1:
                    QUANTITY = askQuantity(PRODUCT)
                    ITEM_TOTAL = itemTotal(PRODUCT, QUANTITY)
                    POINTS = getPoints(BAKING_ITEM)
                    ITEM = item(ITEM_TOTAL, BAKING_ITEM, QUANTITY, POINTS)
                    CART = cart(ITEM, CART)
                    addedToCart()
                    break
                if DIRECTION == 3:
                    break

        if OPERATION == 2:##cart and check out
            if CART == []:
                print("Your Cart is empty")
                continue
            else:
                displayCart(CART)
                TOTAL_COST = totalCost()
                CHECKOUT = askCheckOut()
                ## make option to delete stuff from cart... check contact list thing
               
                if CHECKOUT == "y" or CHECKOUT == "yes" or CHECKOUT == "Y" or CHECKOUT == "Yes":
                    customerAccountManagement(TOTAL_COST) #username and stuff
                    print("You have successfully purchased from The Trendy Market!")
                    updateQuantity(CART)
                
                    purchased(CART)#clearing cart and review
                    continue

                else:
                    continue

        if OPERATION == 3:
                MANAGE = manageMenu()
                if MANAGE == 1:#view past transactions
                    ACCOUNT, ACCOUNT_USERNAME = getAccount()##getting 2D array and account username
                    displayCustomerHistory(ACCOUNT, ACCOUNT_USERNAME)
                
                elif MANAGE == 2:#update quantity
                    manageStock()

                else:
                    continue

        if OPERATION == 4:
                exit()
                    
                    

 