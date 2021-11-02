"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_01_page_114.py
Problem:
        Dịch từng số sau sang số thập phân:
             1. 11001
             2. 100000
             3. 11111
Solution:

"""
# 1: 11001

bitString = '11001'
decimal = 0
exponent = len(bitString) - 1
for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print('Giá trị số nguyên là', decimal)

# 2: 100000

bitString = '100000'
decimal = 0
exponent = len(bitString) - 1
for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print('Giá trị số nguyên là', decimal)

# 3: 11111

bitString = '11111'
decimal = 0
exponent = len(bitString) - 1
for digital in bitString:
    decimal = decimal + int(digital) * 2 ** exponent
    exponent = exponent - 1
print('Giá trị số nguyên là', decimal)





