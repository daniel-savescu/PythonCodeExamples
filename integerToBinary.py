# Program : Integer To Binary Converter
# Python version : 3.9.6

try:    
    numberToConvert = int(input("Enter a integer number to convert into binary: "))
    print("The binary number is: ", bin(numberToConvert).replace("0b", " "))
except ValueError:
    print("Enter only integers !")
