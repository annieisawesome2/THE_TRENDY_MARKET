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

ACCOUNTS = "accounts.db"
DATABASE_FILE = "market.db"
 
FIRST_RUN = True

ITEM = [0, "", 0, 0]
CART = []
# Test if FILENAME already exists
if (pathlib.Path.cwd() / DATABASE_FILE).exists():
   FIRST_RUN = False
 
CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = CONNECTION.cursor()

ACCOUNT_CON = sqlite3.connect(ACCOUNTS)
ACCOUNT_CUR = ACCOUNT_CON.cursor()

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
    ITEM = getInput("Please type in the item you would like to view from the frozen products listed", ["Vanilla Ice Cream", "Chocolate Ice Cream", "Strawberry Ice Cream", "Popsicles", "Frozen Blueberries", "Frozen Strawberries", "Frozen Rasberries", "Frozen Mangoes", "Frozen Pinapples", "Frozen Blackberries", "Frozen Scallops", "Frozen Peas", "Frozen Fillets", "Frozen Prawns", "Frozen Salmon"])
    return ITEM

def selectFruits():
    ITEM = getInput("Please type in the item you would like to view from the fruit products listed", ["Blueberries", "Pinapple","Strawberries","Bananas","Apples","Oranges","Mandarins","Peaches","Green Grapes","Red Grapes","Mangoes","Dragon Fruit","Passion Fruit","Watermelon","Pears","Cherries"])
    return ITEM

def selectVegetables():
    ITEM = getInput("Please type in the item you would like to view from the vegetable products listed", ["Mushrooms","Red Onions","Garlic","Avacados","Green Peppers","Celery","Carrot","Potatoes","Tomatoes","Cucumbers","Lettuce","Cabbage","Green Onions","Romaine Hearts","Peas","Red peppers","Yellow Peppers","Orange Peppers","Zucchini","Kale","Winter Melon","Beets","Corn","Yam","Spinach","Baby Spinach","Broccoli","Squash","Green Bean","Cilantro","Ginger","Turnip","Pumpkin"])
    return ITEM

def selectCondiments():
    ITEM = getInput("Please type in the item you would like to view from the condiment products listed", ["Mustard","Ketchup","Relish","Mayo","Ranch","Honey","Sriracha","Soy Sauce","Olive Oil","Canola Oil","Mayonnaise","Maple Syrup","Hot Sauce","Vinager"])
    return ITEM

def selectBaking():
    ITEM = getInput("Please type in the item you would like to view from the baking products listed", ["Sugar","Salt","Flour","Coca Powder","Baking Powder","Baking Soda","Vanilla Cake Mix","Chocolate Cake Mix","Icing","Butter Cream","Classic Sprinkles","Vanilla Extract","Blue Food Coloring","Yellow Food Coloring","Red Food Coloring","Pink Food Coloring","Green Food Coloring","Icing Sugar","Baking Soda","Chocolate Chips","Almond Extract","Cinnamon","Brown Sugar","Yeast","Red Velvet Cake Mix","Whole Wheat Flour","Cornmeal","Cornstarch"])
    return ITEM

def directionChoice():
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
    ##must check if quantity is less than what is available
    QUANTITY = input("Quantity? ")
    QUANTITY = checkInt(QUANTITY)

    AVAILABLE = PRODUCT[5]
    
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
    REVIEW = input(f"Write your review for {ITEM}: ")
    REVIEW = f'"{REVIEW}",'
    return REVIEW

def getAnyInput(QUESTION):
    INPUT = input(f"Please enter {QUESTION}: ")
    if INPUT == "":
        print("Cannot be left blank")
        return getAnyInput(QUESTION)
    else:
        return INPUT


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

    return PRODUCT

def itemTotal(PRODUCT, QUANTITY):
    TOTAL_FOR_ITEM = PRODUCT[3] * QUANTITY
    return TOTAL_FOR_ITEM

def item(ITEM_TOTAL, MEAT_ITEM, QUANTITY, POINTS):
    ITEM[0] = ITEM_TOTAL
    ITEM[1] = MEAT_ITEM
    ITEM[2] = QUANTITY
    ITEM[3] = POINTS
    return ITEM

def cart(ITEM, CART):
    CART.append(ITEM[:])
    return CART

def addedToCart():
    for i in range(len(CART)):
        PRODUCT = CART[i][1]
        QUANTITY = CART[i][2]

    print(f'''
{PRODUCT}(x{QUANTITY}) is successfully added to cart!
        ''')

def updateQuantity(CART):
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
        print(UPDATED_QUANTITY)
    

def purchased(CART):
    global CURSOR, CONNECTION

    print(CART)
    

    ADD = input("Give a review? Y/n")

    if ADD == "N" or ADD == "n":
        CART = []
        pass

    else:
        for i in range(len(CART)):
            print(f"{i+1}. {CART[i][1]}")

        while True:
            CHOICE = int(input("Pleace input the corresponding number: "))
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

        CART.pop(CHOICE-1)

        if len(CART) == 0:
            return

        return purchased(CART)

def getAccount(ACCOUNT_USERNAME):
    global ACCOUNT_CUR, ACCOUNT_CON
    
    DATA = ACCOUNT_CUR.execute(f'''
        SELECT
            *
        FROM
            {ACCOUNT_USERNAME}
        WHERE
            account = ?
        
    ;''')

    print(DATA)

def makeAccount():
    global ACCOUNT_CUR, ACCOUNT_CON
    ACCOUNT_USERNAME =  getAnyInput("a username with no spaces or special characters")
 

    if  " " in ACCOUNT_USERNAME:
        print("Please enter a valid username with no spaces or special characters!")
        return makeAccount()
    
    elif ACCOUNT_USERNAME.isalnum() == False:
        print("Please enter a valid username with no spaces or special characters!")
        return makeAccount()

    ##section where you choose to create an account  or to checkout with an already existing username
    #elif ACCOUNT_USERNAME == :
        #print("Sorry this username is taken, please enter a new one.")
        #return makeAccount(POINTS, TRANSACTION)

    else:
        ACCOUNT_CUR.execute(f'''
            CREATE TABLE 
                {ACCOUNT_USERNAME} (
                    account TEXT PRIMARY KEY, 
                    points INTEGER, 
                    history TEXT
                    
            )
        ;''')

        ACCOUNT_CON.commit()

def transactionAndPoints(ACCOUNT_USERNAME, POINTS, TRANSACTION):
    global ACCOUNT_CUR, ACCOUNT_CON

    ACCOUNT_CUR.execute(f'''
        INSERT INTO
            {ACCOUNT_USERNAME}
        VALUES (
            ?, ?, ?
        )
    
    ;''', [ACCOUNT_USERNAME, POINTS, TRANSACTION])

    ACCOUNT_CON.commit()


def getPoints(PRODUCT):
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

##--OUTPUTS--##
def intro():
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Trendy Market!! We source the best quality foods from this planet!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

def displayProducts(PRODUCT):
    print(PRODUCT)
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
    for i in range(len(CART)):
        UNIT_PRICE = CART[i][0]
        ITEM = CART[i][1]
        QUANTITY = CART[i][2]
        UNIT_PRICE = "{:.2f}".format(UNIT_PRICE)

    
        print(f"{ITEM}(x{QUANTITY}) = ${UNIT_PRICE}")


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

            if CATEGORY == 1:
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
                
                
            elif CATEGORY == 2:
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

            elif CATEGORY == 3:
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

            elif CATEGORY == 4:
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

            elif CATEGORY == 5:
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
                
            elif CATEGORY == 6:
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
                
            elif CATEGORY == 7:
                BAKING =shopBaking()
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

        if OPERATION == 2:
                print(CART)
                updateQuantity(CART)
                displayCart(CART)
                CHECKOUT = askCheckOut()
                ##point system here
                
               

                if CHECKOUT == "y" or CHECKOUT == "yes" or CHECKOUT == "Y" or CHECKOUT == "Yes":
                    ACCOUNT = input("Do you have an existing account with The Trendy Market?(Y/n)")
                    if ACCOUNT == "n" or ACCOUNT == "N" or ACCOUNT == "no" or ACCOUNT == "No":
                        makeAccount(0, "hi") #points, and cart stuff
                    else:
                        pass


                    ##section where you choose to create an account  or to checkout with an already existing username






                    print("You have successfully purchased from The Trendy Market.")
                    purchased(CART)
                    continue

                else:
                    continue

                #[[31.98, 'Ham', 2], [41.97, 'Bacon', 3]]
                #new quantities would be 13 and 12
                #delete stuff from cart...reference contacts things again  
                #once user checks out, update quantity
                #Subtract quantity from database

        if OPERATION == 3:
                pass
        
        if OPERATION == 4:
                exit()
                    
                    

 