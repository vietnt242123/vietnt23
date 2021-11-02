"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: Projects_01_page_132.py
Problem:
        Write a script that inputs a line of plaintext and a distance value and outputs an
         encrypted text using a Caesar cipher. The script should work for any printable
         characters
Solution:

"""
palainText = input("Nhập một tin nhắn")
distance = int(input("nhập giá trị khoảng cách"))
code = ""
for ch in plainText:
    ordValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)
print(code)


