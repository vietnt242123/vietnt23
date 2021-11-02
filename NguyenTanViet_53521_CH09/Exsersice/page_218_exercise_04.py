"""
Author: NGUYEN TAN VIET
Date: 15/10/2021
Program: exersice_04_page_218.py
Problem :
    Các hàm vẽ đa giác trong mô-đun đa giác có cùng một mẫu, khác nhau
    chỉ ở số cạnh (số lần lặp của vòng lặp). Biến mô hình này thành một mô hình tổng quát hơn
    hàm có tên polygon, lấy số lượng cạnh làm đối số bổ sung.

Solution:
    Nhập số không của các cạnh của đa giác: 10
    Nhập chiều dài các cạnh của đa giác: 100

"""
import turtle

# Tạo bút rùa

t = turtle.Turtle()

# Lấy đầu vào cho các cạnh của đa giác

n = int(input("Enter the no of the sides of the polygon : "))

# Lấy đầu vào cho độ dài các cạnh của đa giác

l = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
