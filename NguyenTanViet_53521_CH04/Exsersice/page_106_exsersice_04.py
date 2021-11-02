"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_03_page_106.py
Problem:
        Giả sử rằng biến myString tham chiếu đến một chuỗi và biến
        reverseString đề cập đến một chuỗi rỗng. Viết một vòng lặp có thêm các ký tự
        từ myString đến reverseString theo thứ tự ngược lại
"""
myString = 'hello'
reverseString = ''

for ch in myString[::-1]:
    reverseString = reverseString + ch
print(reverseString)


