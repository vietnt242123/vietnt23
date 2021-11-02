"""
Author: NGUYEN TAN VIET
Date: 24/010/2021
Program: page_203_project_04.py
Problem:
    Restructure Newton’s method (Case Study 3.6) by decomposing it into three
    cooperating functions. The newton function can use either the recursive strategy
    of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
    limit is assigned to a function named limitReached, whereas the task of computing a new approximation is assigned
    to a function named improveEstimate. Each function expects the relevant arguments and returns an appropriate value

Solution:
    Enter a positive number or enter to quit: 2
    The program's estimate is 1.4142156862745097
    Python's estimate is      1.4142135623730951
    Enter a positive number or enter to quit: 5
    The program's estimate is 2.2360688956433634
    Python's estimate is      2.23606797749979

"""
import math


def limitReached(val, last):
    return abs(val - last) < 0.01


def improveEstimate(val, n):
    return (val + n / val) * 0.5


def newton(n):
    val = n
    while True:
        last = val
        val = improveEstimate(val, n)
        if limitReached(val, last):
            break
    return val


def main():
    """
    :return:
    """
    while True:
        x = input("Enter a positive number or enter to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))


if __name__ == '__main__':
    main()