# Reverse Elements In Python List

originalList = []

numberOfElements = int(input("Enter the number of elements of you want to enter into the list : "))

for index in range(0,numberOfElements):
    elementValue = int(input("Enter element value : \n"))
    originalList.append(elementValue)

print("The original list is : ", originalList)

print("The reversed list is : ", originalList[::-1])





