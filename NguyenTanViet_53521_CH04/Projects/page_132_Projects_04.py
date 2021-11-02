"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: Projects_04_page_132.py
Problem:
        Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.
        py and decimalToOctal.py, which convert numbers between the octal
        and decimal representations of integers. These scripts use algorithms that are
        similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3
Solution:

"""
decimal = int(input("enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient remainder octal")
    ostring = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        ostring = str(remainder) + ostring
        print("%5d%8d%12s" % (decimal, remainder, ostring))
    print("The octal representation is", ostring)

