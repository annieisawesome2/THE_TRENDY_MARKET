LIST = [["31.98", 'Ham', "2"], ["41.97", 'Bacon', "3"]]
DATA = []
print(LIST)

for item in LIST:

    item = "#".join(item)
    print(item)
    DATA.append(item)

print(DATA)
DATA = "$".join(DATA)
DATA = DATA + "*"
print(DATA)

print(DATA.split("$"))

USERNAME = input("Usernamne > ")

PAST_POINT = # get all their past points from database

NEW_POINTS = # get points from new order

UPDATED_POINTS = PAST_POINT + NEW_POINTS

cur.execute - # update old points with new points

# Apply new points to order

cur.execute(f'''
    CREATE TABLE
        {USERNAME} (
            name, 
            address,
            age
        )
    
;''')

con.commit()