"""
Author: NGUYEN TAN VIET
Date: 22/10/2021
Program: exersice_03_page_199.py
Problem:
     Write the code for a reducing that creates a single string from a list of strings named words.

Solution:
hello

"""

from functools import reduce

def add(x, y):

    return x + y
 words = ["h", "e", "l", "l", "o"]

result = reduce(add, words)
print(result)
