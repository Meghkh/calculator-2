"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    input_string = raw_input(">> ")
    tokens = input_string.split()

    if tokens[1]:
        operand1 = float(tokens[1])
        if len(tokens) == 3:
            operand2 = float(tokens[2])

    if tokens[0] == 'q':
        break
    else:
        if tokens[0] == "+":
            print add(operand1, operand2)
        elif tokens[0] == "-":
            print subtract(operand1, operand2)
        elif tokens[0] == "*":
            print multiply(operand1, operand2)
        elif tokens[0] == "/":
            print divide(operand1, operand2)
        elif tokens[0] == "square":
            print square(operand1)
        elif tokens[0] == "cube":
            print cube(operand1)
        elif tokens[0] == "pow":
            print power(operand1, operand2)
        elif tokens[0] == "mod":
            print mod(operand1, operand2)
        else:
            print "Input not recognized"
