"""
Author: NGUYEN TAN VIET
Date: 15/10/2021
Program: exersice_03_page_218.py
Problem:
    Thêm một chức năng có tên vòng tròn vào mô-đun đa giác. Hàm này mong đợi
    đối số tương tự như các hàm vuông và lục giác. Hàm sẽ vẽ một
    khoanh tròn. (Gợi ý: vòng lặp lặp lại 360 lần.)

Solution:

"""

import turtle

def polygon(t, length, n):

    for _ in range(n):
        t.fd(length)
        t.lt(360 / n)

bob = turtle.Turtle()

 Bob.penup()
 bob.sety(-270)
 bob.pendown()
 polygon(bob, 30, 60)
 turtle.mainloop()




