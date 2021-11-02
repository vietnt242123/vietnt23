"""
Author: Nguyen Tan Viet
Date: 08/09/2021
Program: exersice_04_page_72.py
Problem:
        Viết một vòng lặp xuất ra các con số trong danh sách có tên là tiền lương. Đầu ra phải
          định dạng trong một cột hợp lý, với chiều rộng trường là 12 và độ chính xác là 2.
Solution:

"""
salaries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in salaries:
    print("your salaries $%12.2f" % x)

