"""
Program: Projects_04_page_240.py
Author: NGUYEN TAN VIET
Date: 16/10/2021

Problen:
    he Koch bông tuyết là một hình dạng fractal. Tại mức 0, hình dạng là một góc tri giác đều. Ở cấp độ 1,
mỗi đoạn thẳng được chia thành bốn phần bằng nhau, tạo ra
vết lồi đều ở giữa mỗi đoạn. Hình 7-15 cho thấy những hình dạng này
ở các cấp 0, 1 và 2.Ở cấp cao nhất, tập lệnh sử dụng một hàm drawFractalLine để vẽ ba Fractal
các dòng. Mỗi đường được xác định bởi một khoảng cách, hướng (góc) và mức cho trước. Các
các góc ban đầu là 0, 2120 và 120 độ. Khoảng cách ban đầu có thể là bất kỳ kích thước nào,
chẳng hạn như 200 pixel. Hàm drawFractalLine là hàm đệ quy. Nếu mức là 0,
thì con rùa di chuyển quãng đường đã cho theo hướng cho trước. Nếu không
hàm vẽ bốn đường gãy khúc với một phần ba khoảng cách đã cho, các góc
tạo ra hiệu ứng đã cho và mức đã cho trừ đi 1. Viết một kịch bản thu hút
bông tuyết Koch.

Solution:

"""

from time import sleep
from turtle import Turtle


def drawKochFractal(width, height, size, level):
    """Vẽ một fractal Koch có cấp độ và kích thước nhất định."""
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)


def drawFractalLine(t, distance, theta, level):

    """Vẽ một đường đơn theo một hướng nhất định
       hoặc bốn đường fractal theo các hướng mới."""
    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance // 3, theta, level - 1)
        drawFractalLine(t, distance // 3, theta + 60, level - 1)
        drawFractalLine(t, distance // 3, theta - 60, level - 1)
        drawFractalLine(t, distance // 3, theta, level - 1)


def drawPolarLine(t, distance, theta):

    """Di chuyển khoảng cách đã cho theo hướng nhất định."""
    t.setheading(theta)
    t.forward(distance)


if __name__ == '__main__':
    level = int(input("Nhập cấp độ: "))
    drawKochFractal(200, 200, 150, level)
    sleep(5)
