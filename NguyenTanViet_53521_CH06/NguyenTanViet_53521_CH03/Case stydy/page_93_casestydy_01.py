"""
Program: page_93_casestydy_01.py
Author: Nguyen Tan Viet
Date: 18/09/2021
       Compute the square root of a number.
     1. The input is a number.
     2. The outputs are the program's estimate of the square root
        using Newton's method of successive approximations, and
        Python's own estimate using math.sqrt.
"""
import math
# Nhận số đầu vào từ người dùng
x = float(input("Nhập một số dương: "))

# Khởi tạo đúng sai và ước tính
tolerance = 0.000001
estimate = 1.0

# Thực hiện các phép tính gần đúng liên tiếp
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
       break

# Xuất ra kết quả
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(x))


