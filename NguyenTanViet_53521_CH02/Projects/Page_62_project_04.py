"""
Author: NGUYEN TAN VIET
Date: 03/09/2021
Program: page_62_project_04.py
Problem:
       Viết chương trình lấy bán kính của một hình cầu (một số dấu phẩy động) là
       đầu vào và sau đó xuất ra đường kính, chu vi, diện tích bề mặt


Solution:

"""
a = 3.14
rad = float(input("Nhập bán kính: "))
d = rad * 2 * a
s = 4 * a * pow(rad, 2)
print("Đường kính: ", d, "m")
print("Diện tích: ", s, "m2")




