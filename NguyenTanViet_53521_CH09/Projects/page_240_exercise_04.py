"""
Author: NGUYEN TAN VIET
Date: 15/10/2021
Program: Projects_04_page_240.py
Problen:
 Nghệ sĩ người Hà Lan ở thế kỷ 20, Piet Mondrian, đã phát triển một phong cách trừu tượng
bức tranh thể hiện các mẫu đệ quy đơn giản. Để tạo ra một mẫu như vậy
với máy tính, người ta sẽ bắt đầu bằng một hình chữ nhật được tô màu ngẫu nhiên và
sau đó liên tục điền vào hai phần nhỏ không bằng nhau bằng các màu ngẫu nhiên,
Như bạn có thể thấy, thuật toán tiếp tục quá trình chia nhỏ cho đến "thời điểm phù hợp về mặt thẩm mỹ"
đạt được. Trong phiên bản này, thuật toán chia hình chữ nhật hiện tại thành các phần đại diện cho 1/3 và 2/3
của khu vực của nó và xen kẽ các phân khu này theo trục ngang và trục dọc. Thiết kế, triển khai và
kiểm tra tập lệnh sử dụng hàm đệ quy để vẽ các mẫu này.

Solution:

Nhập cấp độ: 10

"""
import random
from turtle import Turtle
from time import sleep



def fillRectangle(t, x1, y1, x2, y2):

    """Điền vào một hình chữ nhật với các điểm góc đã cho
       sử dụng một màu ngẫu nhiên."""

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()


def mondrian(t, x1, y1, x2, y2, level):

    """Vẽ một bức tranh giống Mondrian ở cấp độ đã cho."""

    if level > 0:
        fillRectangle(t, x1, y1, x2, y2)

        vertical = random.randint(1, 2)

        if vertical == 1:  # Vertical split
            mondrian(t, x1, y1, (x2 - x1) / 3 + x1, y2,
                     level - 1)
            mondrian(t, (x2 - x1) / 3 + x1, y1, x2, y2,
                     level - 1)

        else:  # Horizontal split

            mondrian(t, x1, y1, x2, (y2 - y1) / 3 + y1,
                     level - 1)
            mondrian(t, x1, (y2 - y1) / 3 + y1, x2, y2,
                     level - 1)


def main():
    level = int(input("Nhập cấp độ: "))
    t = Turtle()
    t.hideturtle()
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    mondrian(t, -width, height,
             width, -height, level)
    sleep(5)


main()

