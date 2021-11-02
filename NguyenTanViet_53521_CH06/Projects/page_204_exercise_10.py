"""
Author: NGUYEN TAN VIET
Date: 24/010/2021
Program: page_204_project_10.py
Problem:
     Define and test a function myRange. This function should behave like Python’s
     standard range function, with the required and optional arguments, but it should
     return a list. Do not use the range function in your implementation! (Hints:
     Study Python’s help on range to determine the names, positions, and what to do
     with your function’s parameters. Use a default value of None for the two optional
     parameters. If these parameters both equal None, then the function has been
     called with just the stop value. If just the third parameter equals None, then the
     function has been called with a start value as well. Thus, the first part of the function’s code establishes what
     the values of the parameters are or should be. The rest of the code uses those values to build a list by counting
     up or down.)

Solution:
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

def myRange(first, second=None, step=1):
    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    output = []
    while current < end:
        output.append(current)
        current += step

    return output


r = myRange(10)
print(r)
