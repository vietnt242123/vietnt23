"""
Program: Projects_04_page_240.py
Author: NGUYEN TAN VIET
Date: 16/10/2021

Problen:
    Định nghĩa một hàm drawCircle. Hàm này sẽ mong đợi một đối tượng Turtle,
    tọa độ của điểm trung tâm của vòng tròn và bán kính của vòng tròn dưới dạng các điểm đối số.
    Hàm sẽ vẽ một vòng tròn được chỉ định. Thuật toán nên
    vẽ chu vi của hình tròn bằng cách quay 3 độ và di chuyển khoảng cách 120 lần.
    Tính quãng đường đã di chuyển với công thức 2.0 * p * bán kính / 120.0.

Solution:

"""
import math
from turtle import Turtle
from time import sleep

def drawCircle(t, x, y, radius):

    """Vẽ một đường tròn với tâm và bán kính đã cho."""
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)


def main():
    """Cho phép người dùng nhập điểm trung tâm và bán kính."""
    x = int(input("Nhập tọa độ x của điểm trung tâm: "))
    y = int(input("Nhập tọa độ y của điểm trung tâm: "))
    radius = int(input("Nhập bán kính: "))
    drawCircle(Turtle(), x, y, radius)
    sleep(5)


if __name__ == '__main__':
    main()
