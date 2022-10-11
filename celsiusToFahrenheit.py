# Program : Convert Celsius to Fahrenheit
# Python Version : 3.9.6

# Formula : (Celsius x 1.8) + 32

try:
    celsius = float(input("Enter Celsius degrees: "))
    print("The temperature in Fahrenheit is : ", ((celsius * 1.8)+32))
except ValueError:
    print("Please enter floating point / integer number.")
