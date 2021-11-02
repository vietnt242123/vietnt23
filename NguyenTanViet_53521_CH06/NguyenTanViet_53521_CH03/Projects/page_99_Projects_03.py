"""
Author: Nguyen Tan Viet
Date: 15/09/2021
Program: exersice_03_page_99.py
Problem:
        Điều gì xảy ra khi lập trình viên quên cập nhật biến điều khiển vòng lặp trong
                                một vòng lặp trong khi?
Solution:

"""
import random
so_lon = int(input("Mời nhập số lớn: "))
so_be = int(input("Mời nhập số bé: "))
luot = 0
while True:
    luot += 1
    num = (so_be + so_lon) // 2
    print("Số bạn là %d" %num)
    luot_choi = input("Nhập =,<,>: ")
    if luot_choi == "=":
        print("Chúc mừng bạn chiến thắng, số lượt của bạn dùng là: ", luot)
    elif luot_choi == ">":
        so_lon = num + 1
    elif luot_choi == "<":
        so_be = num - 1
    else:
        print("Trò chơi kết thúc: ")
        break




