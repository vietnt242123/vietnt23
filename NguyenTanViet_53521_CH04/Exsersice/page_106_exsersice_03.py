"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_03_page_106.py
Problem:
        Giả sử rằng biến myString tham chiếu đến một chuỗi. Viết một đoạn mã
        sử dụng một vòng lặp để in các ký tự của chuỗi theo thứ tự ngược lại.

"""
# vòng lặp đếm ngược kí tự trong chuỗi
myString = 'hello'
for ch in myString[::-1]:
    pring(ch)

