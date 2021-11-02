"""
Author: NGUYEN TAN VIET
Date: 24/010/2021
Program: page_203_project_02.py

Problem:
      Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton.
      (Hint: The estimate of the square root should be passed as a second argument to the function.)
Solution:

2.0000000929222947

"""
approximating = 0.000001


def newton2(x, estimate):
    """
    Calculate approximating square
    :param estimate:
    :param x: enter a number to calculate approximating square
    :return: the estimate of its square root
    """
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference > approximating:
        estimate = newton2(x, estimate)
    return estimate


print(newton2(4, 1))