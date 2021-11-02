"""
Author: Nguyen Tan Viet
Date: 18/09/2021
Program: Project_06_page_100.py
Problem:Nhà toán học người Đức Gottfried Leibniz đã phát triển phương pháp sau
để gần đúng giá trị của π:
π / 4 5 1] 1/3 1 1/5] 1/7 1. . .
Viết một chương trình cho phép người dùng chỉ định số lần lặp được sử dụng trong
ước tính này và hiển thị giá trị kết quả.

Solution:

"""
pi = 0
for x  in range(1, 1000, 2):
    if x % 4 == 1:
        p1 = pi + (1/x)
    else:
        p1 = pi - (1/x)
pi = pi * 4
print(pi)

