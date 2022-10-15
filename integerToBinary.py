# Program : Integer To Binary Converter

try:    
    numberToConvert = int(input("Enter a integer number to convert into binary: "))
    print("The binary number is: ", bin(numberToConvert).replace("0b", " "))
except ValueError:
    print("Enter only integers !")
