

def add(input_list): 
    for x in input_list: # sum elements in the list with a loop
        x = int(x)
        sum(x)


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least 1 argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return float(num1) ** float(num2)  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2

add([2,3,4,6])
