"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_02_page_114.py
Problem:
       Dịch từng số sau sang số nhị phân:
             x. 47
             y. 127
             z. 64

Solution:

"""
# x. 47
decimal = int('47')
bitString = ''
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
    print('%5d%8d%12s'%(decimal, remainder, bitString))
print('Số nhị phân là:', bitString)

# y. 127
decimal = int('127')
bitString = ''
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
    print('%5d%8d%12s'%(decimal, remainder, bitString))
print('Số nhị phân là:', bitString)

# z. 64

decimal = int('64')
bitString = ''
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
    print('%5d%8d%12s'%(decimal, remainder, bitString))
print('Số nhị phân là:', bitString)






