"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_04_page_149.py
Problem:
      Xác định một hàm có tên là tổng kết. Hàm này mong đợi hai số, được đặt tên là
      thấp và cao, như các đối số. Hàm tính toán và trả về tổng của
                     con số giữa thấp và cao, bao gồm.
Solution:

"""

low = int(input('Nhập thấp: '))
high = int(input('Nhập cao: '))
def summation():
    sum = 0
    for i in (low, high):
        sum += i
    print(sum)
    summation()
