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