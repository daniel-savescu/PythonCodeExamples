# ------------------------------------------------
# Project: Shopping List
# Version: 1.0.1
# Year: 2022
# =-----------------------------------------------

# Imports libraries ==============================
from curses.ascii import isalpha
from datetime import date
from multiprocessing.sharedctypes import Value
from typing import Type
# ================================================


# Variables ======================================
today = date.today()
shoppingList = []
shoppingListPrice = []
shoppingDict = {}
total = 0.00
item_price = 0
# ================================================

# Insert items ===================================


while True:
    print("\n============SHOPPING LIST============\n")
    print("TO QUIT THE APPLICATION TYPE : 'quit'\n")
    print("TYPE : 'remove' to delete an item from the .\n\n")
    for k in shoppingList:
        print("You have added the product: " + k)

    item_to_buy = input("\n\tInsert item > ").lower()
    if item_to_buy == 'quit':
        break
    elif item_to_buy != 'remove':
        try:
            item_price = float(input("\tPrice: "))
        except ValueError:
            print("Type only numbers!")
        shoppingListPrice.append(str(item_price))
    shoppingList.append(item_to_buy)
    if item_to_buy == 'remove':
        shoppingList.remove(item_to_buy)
        item_to_buy = input("\n\tDelete item > ").lower()
        if item_to_buy not in shoppingList:
            print("\n\tItem not in list")
        else:
            shoppingList.remove(item_to_buy)
        
            
   

# =================================================


# Dictionary ======================================
shoppingDict = {}
for key in shoppingList:
    for value in shoppingListPrice:
        shoppingDict[key] = value
        shoppingListPrice.remove(value)
        break
# =================================================

# Printing result =================================
for keys, value in shoppingDict.items():
    print("You have added the product: " + keys + " | price: " + value)
# =================================================


# Calculate the total =============================
for keys, value in shoppingDict.items():
    # replace ',' with '.' for price value.
    total += float(value.replace(',', '.'))
print("Total is: " + str(float(total)))
# =================================================


# Create file if not exist ========================
# Add list in text file ===========================
# Append 'items'
file = open("items.txt", "a")
for keys, value in shoppingDict.items():
    file.write("Date: " + today.strftime("%B %d, %Y") +
               " | Product: " + keys + " | Price: " + value + "\n")
print("---------------------------------")
print("TOTAL: " + str(float(total)))
file.write("---------------------------------\n" +
           "TOTAL: " + str(float(total))+"\n\n\n")
file.close()
# =================================================
