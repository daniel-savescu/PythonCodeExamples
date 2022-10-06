#Shopping List

shoppingList = []

print("============SHOPPING LIST============\n\n")
print("TO QUIT THE APPLICATION TYPE : 'quit'\n\n")


while True:

    item_to_buy = input("Insert item > ").lower()

    if item_to_buy == 'quit':
        break

    shoppingList.append(item_to_buy)

print("\n\nThe list content is : \n\n")

for item in shoppingList:
    
    print(item + "\n\n")
   