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
    tokens = input.split(" ")
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    if tokens[0] == "+":
        print add(num1,num2)
        value_returned = True