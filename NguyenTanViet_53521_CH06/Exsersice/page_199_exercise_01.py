"""
Author: NGUYEN TAN VIET
Date: 22/10/2021
Program: exersice_01_page_199.py
Problem:
     Write the code for a mapping that generates a list of the absolute values of the numbers in a list
                                             named number

Solution:

[1, 2, 66, 79]

"""
numbers = [1, -2, -66, 79]
result = list(map(abs, numbers))
print(result)