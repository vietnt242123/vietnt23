"""
Program: Projects_04_page_240.py
Author: NGUYEN TAN VIET
Date: 16/10/2021

Problen:
    Sửa đổi chương trình nghiên cứu điển hình của chương này (đường cong c) để nó vẽ đường thẳng
                           phân đoạn sử dụng màu sắc ngẫu nhiên
Solution:

"""

from turtle import *

def line(t, x1, y1, x2, y2):

    """vẽ đoạn thẳng từ x1,y1 to x2,y2"""

    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

def drawLine(t, x1, y1, x2, y2, level):

    """tạo thành hình dạng"""

    if level == 0:
        line(t, x1, y1, x2, y2)
    else:
        xm = ((x1 + x2) + (y2 - y1)) // 2
        ym = ((y1 + y2) + (x1 - x2)) // 2
        drawLine(t, x1, y1, xm, ym, level-1)
        drawLine(t, xm, ym, x2, y2, level-1)

def main():
    """chức năng chính"""

    myTurtle = Turtle()

    myTurtle.hideturtle()

    num = int(input("Vui lòng nhập số cấp độ: "))

    drawLine(myTurtle, 100, 0, 100, -200, num)


main()

