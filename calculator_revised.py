"""A prefix-notation calculator."""

from arithmetic_revised import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print "You will exit."
        break

    elif len(tokens) < 2:
        print "Not enough inputs."
        continue

    operands = []
    operator = tokens[0]
    for i in range(1, len(tokens)):
        operands.append(tokens[i])

    # if len(tokens) < 3:
    #     num2 = "0"

    # else:
    #     num2 = tokens[2]

    # if len(tokens) > 3:
    #     num3 = tokens[3]

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    result = None

    for i in range(len(operands)):
        if not operands[i].isdigit():
            print "Invalid inputs found!"
        continue

    if operator == "+":
        result = add(operands)

    elif operator == "-":
        result = subtract(operands)

    elif operator == "*":
        result = multiply(operands)

    elif operator == "/":
        result = divide(operands)

    elif operator == "square":
        result = square(operands)

    elif operator == "cube":
        result = cube(operands)

    elif operator == "pow":
        result = power(operands)

    elif operator == "mod":
        result = mod(operands)

    elif operator == "x+":
        result = add_mult(operands)

    elif operator == "cubes+":
        result = add_cubes(operands)

    else:
        result = "Please enter an operator followed by any number of integers."

    print result
