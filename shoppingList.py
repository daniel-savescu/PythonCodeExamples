# ------------------------------------------------
# Project: Shopping List
# Version: 1.0.1
# Year: 2022
# =-----------------------------------------------

# Imports libraries ==============================
from datetime import date
# ================================================


# Variables ======================================
today = date.today()
shoppingList = []
# ================================================


# Insert items ===================================
print("============SHOPPING LIST============\n\n")
print("TO QUIT THE APPLICATION TYPE : 'quit'\n\n")

while True:
    item_to_buy = input("Insert item > ").lower()
    if item_to_buy == 'quit':
        break
    shoppingList.append(item_to_buy)
print("\n\nThe list content is : \n\n")
# =================================================


# Create file if not exist ========================
# Add list in text file ===========================
# Append 'items'
for item in shoppingList:
    with open("items.txt", "a") as file_object:
        file_object.write(
            "Date: " + today.strftime("%B %d, %Y") +
            "\tItem: " + item + "\n")
# =================================================
