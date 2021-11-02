"""
Author: Nguyen Tan Viet
Date: 12/09/2021
Program: Projects_01_page_99.py
Problem:
        Viết chương trình nhận độ dài ba cạnh của tam giác làm đầu vào.
        Kết quả đầu ra của chương trình phải cho biết tam giác có phải là
        cạnh đều hay không Tam giác
Solution:

"""
a = float(input("nhập cạnh a: "))
b = float(input("nhập cạnh b: "))
c = float(input("nhập cạnh c: "))
if a == b == c:
    print(" là tam giác cân. ")
else:
    print("không phải là tam giác cân.")


