# Program : Read Three Intereger And Find The Miminum Value
# Python version : 3.9.6 

try:
    
    a = int(input("Enter first number: "))
    
    b = int(input("Enter second number: "))
    
    c = int(input("Enter third number: "))
    
    minimumValue = a if a < b and a < c else b if b < c else c
    
    print("The minimul value is : " , minimumValue)

except ValueError:
    
    print("Please enter a integer!")



