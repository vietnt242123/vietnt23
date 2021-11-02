"""
Author: NGUYEN TAN VIET
Date: 20/10/2021
Program: exersice_04_page_182.py

Problem:
 Explain what happens when the following recursive function is called with the value 4 as an argument:
def example(n):
   if n > 0:
        print(n)
        example(n - 1)

Solution:
- First, function will check condition. With value = 4 > 0, function will run and print 4.
- Second, function example is called, that is recursion. Currently, n = 3 and print 3
- Continue,.... n = 2 and n = 1 will printed.
- When, n = 0, don't satisfy condition, program will stop.

"""