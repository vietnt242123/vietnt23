"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: Projects_02_page_132.py
Problem:
        Write a script that inputs a line of encrypted text and a distance value and outputs
        plaintext using a Caesar cipher. The script should work for any printable characters
Solution:

"""
code = input ("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherVlue = ordValue - distance
    if cipherVlue < 0:
        cipherVlue = 127 - \
                     (distance - (1 -ordValue))
    plainText += chr(cipherVlue)
print(plainText)

