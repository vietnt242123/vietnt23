"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_04_page_70.py
Problem:
        Dịch từng số sau sang số thập phân:
              a. 47
              b. 127
              c. AA

Solution:

"""
hex = '47'
decimal = 0
exponent = len(hex) - 1
for decimal in hex:
    decimal = decimal + int(digital) * 2 **exponent
    exponent = exponent - 1
print("số thập phân", decimal)






