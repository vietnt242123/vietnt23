"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_04_page_115.py
Problem:
       Dịch từng số sau sang số thập phân:
             a. 47
             b. 127
             c. 64

Solution:

"""
ocString = '47'
decimal = 0
exponent = len(ocString) - 1
for digital in ocString:
    decimal = decimal + int(digital) * 8 ** exponent
    exponent = exponent - 1
print('Số thập phân là', decimal)

ocString = '127'
decimal = 0
exponent = len(ocString) - 1
for digital in ocString:
    decimal = decimal + int(digital) * 8 ** exponent
    exponent = exponent - 1
print('Số thập phân là', decimal)

ocString = '64'
decimal = 0
exponent = len(ocString) - 1
for digital in ocString:
    decimal = decimal + int(digital) * 8 ** exponent
    exponent = exponent - 1
print('Số thập phân là', decimal)










