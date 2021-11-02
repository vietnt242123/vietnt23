"""
Author: Nguyen Tan Viet
Date: 12/09/2021
Program: Projects_02_page_99.py
Problem:
        Viết chương trình nhận độ dài ba cạnh của tam giác làm đầu vào.
        Kết quả đầu ra của chương trình sẽ cho biết tam giác có phải là góc tri vuông hay không.
        Nhắc lại định lý Pitago rằng trong một tam giác vuông, bình phương của
        một cạnh bằng tổng bình phương của hai cạnh còn lại.
Solution:

"""
a = float(input("nhập cạnh a: "))
b = float(input("nhập cạnh b: "))
c = float(input("nhập cạnh c: "))
if a + b == c**2:
    print(" là tam giác cân. ")
elif a + c == b**2:
    print(" là tam giác cân. ")
elif b + c == a**2:
    print(" là tam giác cân. ")
else:
    print("không phải là tam giác cân.")
