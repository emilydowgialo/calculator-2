"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
value_returned = False


while value_returned == False:
    input = raw_input("> ") 
    tokens = input.split(" ") # parsing user's input by space
    num1 = int(tokens[1]) # converting user input into integer
    num2 = int(tokens[2]) # converting user input into integer

    if tokens[0] == "+": # add function 
        print add(num1,num2) # calling the add function from arithmetic.py module
        value_returned = True # breaking the loop

    if tokens[0] == "-":  # subtract function
        print subtract(num1, num2) # calling the subtr function from arithmetic.py module
        value_returned = True # breaking the loop

    if tokens[0] == "*": # multiply function
        print multiply(num1, num2) # calling the multiply function from arithmetic.py module
        value_returned = True # breaking the loop

    if tokens[0] == "/":  # divide function
        print divide(num1, num2) # calling the divide function from arithmetic.py module
        value_returned = True # breaking the loop

    if tokens[0] == "square":
        print square(num1)
        value_returned = True