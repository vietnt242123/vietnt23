"""
Author: Nguyen Tan Viet
Date: 08/09/2021
Program: exersice_05_page_85.py
Problem:
        Giải thích cách kiểm tra số đầu vào không hợp lệ và ngăn nó được sử dụng trong
                  chương trình. Bạn có thể cho rằng người dùng nhập một số
Solution:

"""
x = float(input("nhập số x: "))
y = float(input("nhập số y: "))
z = input("nhập dấu phép tính: ")
a = 0
if z == "+":
    a = x + y
elif z == "-":
    a = x - y
elif z == "*":
    a = x * y
elif z == "/":
    a = x / y
elif z == "%":
    a = x % y
elif z == "**":
    a = x ** y
else:
    print("không hợp lệ nhập lại")
print(x, str(z), y, "=", a)



