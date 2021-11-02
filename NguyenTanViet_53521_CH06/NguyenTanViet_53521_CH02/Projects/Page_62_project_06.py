"""
Author: NGUYEN TAN VIET
Date: 03/09/2021
Program: page_62_project_06.py
Problem:
       Động năng của một vật chuyển động được cho bởi công thức KE 1 2 / mv 5 2 ()
       trong đó m là khối lượng của vật thể và v là vận tốc của nó. Sửa đổi chương trình bạn đã tạo
       trong Dự án 5 để nó in động năng của vật thể cũng như động lượng của nó
Solution:

"""
m = float(input(" Nhập khối lượng:"))
v = float(input("Nhập vận tốc: "))
k = (0.5 * m * (v**2))
p = m * v
print("Động năng là: ", k, "J")
print("Động lượng là: ", p, "N.s")







