"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


def calc_function():
    value_returned = False
    calculating = True
    while calculating == True:
        while value_returned == False:
            input = raw_input("> ") 
            tokens = input.split(" ") # parsing user's input by space
            num1 = int(tokens[1]) # converting user input into integer
            
            if len(tokens) > 2: # accomodates additional parameters
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

            if tokens[0] == "cube":
                print cube(num1)
                value_returned = True

            if tokens[0] == "pow":
                print power(num1, num2)
                value_returned = True

            if tokens[0] == "mod":
                print mod(num1, num2)
                value_returned = True

        continue_playing = raw_input("Would you like to continue calculating? Type 1 for yes and type 2 for no: ")
        if continue_playing == "1":
            value_returned = False
        elif continue_playing == "2":
            calculating = False
            print "goodbye"
        else:
            print "Error: you did not type 1 or 2!"

calc_function()



