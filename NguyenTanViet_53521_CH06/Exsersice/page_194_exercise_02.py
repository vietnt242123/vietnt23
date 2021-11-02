"""
Author: NGUYEN TAN VIET
Date: 22/10/2021
Program: exersice_02_page_194.py

Problem:
     What is the scope of a variable? Give an example.
Solution:
 - Scope refers to the visibility of variables. In other words, which parts of your program can see or use it.
     Normally, every variable has a global scope. Once defined, every part of your program can access a variable.
    - Example:
        x = 5
        def f():
         x = 10 # Attempt to reset x
        f() # Does the top-level x change?
        print(x) # No, this displays 5
        Because scope x when global, x = 5. But in function f(), x is changed into 10. So, in function f, x = 10.
        Out function f, x = 5.

"""