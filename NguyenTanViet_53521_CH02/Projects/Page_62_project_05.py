"""
Author: NGUYEN TAN VIET
Date: 03/09/2021
Program: page_62_project_05.py
Problem:
       Động lượng của một vật thể là khối lượng của nó nhân với vận tốc. Viết chương trình
       chấp nhận khối lượng của một vật thể (tính bằng kilôgam) và vận tốc (tính bằng mét trên giây) là
       đầu vào và sau đó đầu ra động lượng của nó
Solution:

"""
a = float(input("Nhập khối lượng:"))
b = float(input("Nhập động năng: "))
speed = (b/(0.5 * a))
print("Vận tốc = :", speed, "m/s")

