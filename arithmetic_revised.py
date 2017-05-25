"""
    Revised arithmetic file to handle any number of number inputs

"""

def add(lst):
    """ Return the sum of the list of integers with any number of inputs """

    total_sum = 0
    for i in range(len(lst)):
        total_sum = total_sum + float(lst[i])
    return total_sum

def subtract(lst):
    """ Return the difference of the list of integers with any number of inputs """

    total_difference = float(lst[0])
    for i in range(1, len(lst)):
        total_difference = total_difference - float(lst[i])
    return total_difference

def multiply(lst):
    """ Return the product of the list of integers with any number of inputs """

    total_product = 1
    for i in range(len(lst)):
        total_product = total_product * float(lst[i])
    return total_product

def divide(lst):
    """ Return the quotient of the list of integers with any number of inputs """

    total_quotient = float(lst[0])
    for i in range(1, len(lst)):
        total_quotient = total_quotient / float(lst[i])
    return total_quotient

def square(lst):
    """ Return the square of the sum of any number of inputs """

    return (add(lst)) ** 2

def cube(lst):
    """ Return the cube of the sum of any number of inputs """

    return add(lst) ** 3

def power(lst):
    """ Return the result of continuously raising the inputs to the power of the
        next input """

    result = float(lst[0])
    for i in range(1, len(lst)):
        result = result ** (float(lst[i]))
    return result

def mod(lst):
    """ Return the remainder of the division of continuously modding the next input in the list """

    result = float(lst[0])
    for i in range(1, len(lst)):
        result = result % float(lst[i])
    return result
