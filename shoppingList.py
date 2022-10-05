#Shopping List

shoppingList = []

applicationStatus = True

while applicationStatus:

    item = input("Insert item in the shopping list: ").lower()

    shoppingList.append(item)

    print("You have in the shopping list: ", shoppingList)

    promptDelete = input("Do you want to delete an item from the list? 'Yes' / 'No' : ").lower()

    if promptDelete == "yes":

        itemToDelete = input("Enter the name of the item you want to delete: ").lower()

        if itemToDelete not in shoppingList:

            print("Item is not in list!")

        else:

            shoppingList.remove(itemToDelete)

            print("The new list content is: ", shoppingList)
    else:
        
        quit =  input("Quit application? 'Yes' / 'No' : ").lower()

        if quit == "yes":

            applicationStatus = False

