"""
Author: NGUYEN TAN VIET
Date: 20/10/2021
Program: exersice_02_page_182.py

Problem:

 The factorial of a positive integer n, fact(n), is defined recursively as follows:
        fact(n) = 1 , when n = 1
        fact(n) n * fact (n-1)  , otherwise
 Define a recursive function fact that returns the factorial of a given positive integer

Solution:

Enter n to calculate: 3
Factorial of 3 is: 6

"""
number = int(input("Enter n to calculate: "))


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


result = fact(number)
print(f"Factorial of {str(number)} is: " + str(result))