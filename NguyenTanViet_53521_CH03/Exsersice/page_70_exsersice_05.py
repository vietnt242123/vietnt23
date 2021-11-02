"""
Author: Nguyen Tan Viet
Date: 08/09/2021
Program: exersice_05_page_70.py
Problem:
       Giả sử rằng chuỗi kiểm tra biến tham chiếu đến một chuỗi. Viết một vòng lặp in ra
               mỗi ký tự trong chuỗi này, theo sau là giá trị ASCII của nó
Solution:

"""
x = int(input("nhập số vào:" ))
if x <= 120:
    chr(x)
    print("chuổi của bạn: ", chr(x))
else:
    print("lỗi")


