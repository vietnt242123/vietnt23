"""
Author: NGUYEN TAN VIET
Date: 15/10/2021
Program: exersice_01_page_145.py
Problem:
    Lớp Turtle bao gồm một phương thức có tên là vòng tròn. Nhập lớp Rùa, chạy
    trợ giúp (Turtle.circle) và nghiên cứu tài liệu. Sau đó, sử dụng phương pháp này để
    vẽ một vòng tròn đầy và một nửa mặt trăng.

Solution:

"""
import turtle

turtle.Screen()
turtle.bgcolor("magenta")
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(130, 180)
turtle.end_fill()
turtle.hideturtle()
