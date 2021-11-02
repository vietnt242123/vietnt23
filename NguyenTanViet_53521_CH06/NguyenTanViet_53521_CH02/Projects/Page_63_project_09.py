"""
Author: NGUYEN TAN VIET
Date: 03/09/2021
Program: page_63_project_09.py
Problem:
      Viết một chương trình lấy đầu vào là một số km và in ra số hải lý tương ứng. Sử dụng các giá trị gần đúng sau:
      • Một kilomet đại diện cho 1 / 10.000 khoảng cách giữa Bắc Cực và
                đường xích đạo.
      • Có 90 độ, mỗi cung có 60 phút, giữa hướng Bắc
               Cực và đường xích đạo.
      • Một hải lý là 1 phút của một cung tròn.

Solution:

"""
km = float(input("Enter the amount of kilometers:"))

degreesPerMin = 90*60

onekilo = degreesPerMin/10000

nauticalmile = onekilo * km

print("Kilometers,is,nauticalmile: = ", nauticalmile, "nauticalmiles")






