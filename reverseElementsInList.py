# Reverse Elements In Python List
# Python verios : 3.9.6

originalList = []

try:
    numberOfElements = int(input("Enter the number of elements of you want to enter into the list : "))
except ValueError:
    print("Enter only integer")
for index in range(0,numberOfElements):
    elementValue = int(input("Enter element value : \n"))
    originalList.append(elementValue)

print("The original list is : ", originalList)

print("The reversed list is : ", originalList[::-1])





