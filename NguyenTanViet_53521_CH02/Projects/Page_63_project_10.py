"""
Author: NGUYEN TAN VIET
Date: 03/09/2021
Program: page_63_project_09.py
Problem:Tổng tiền lương hàng tuần của một nhân viên bằng tiền lương theo giờ nhân với tổng
số giờ bình thường cộng với bất kỳ khoản tiền làm thêm giờ nào. Lương làm thêm giờ bằng tổng
số giờ làm thêm nhân với 1,5 lần tiền lương theo giờ. Viết một chương trình
lấy làm đầu vào là tiền lương theo giờ, tổng số giờ bình thường và tổng số giờ làm thêm và
hiển thị tổng tiền lương hàng tuần của một nhân viên


Solution:

"""
name = input('Nhập tên nhân viên: ')
h = float(input('Nhập số giờ đi làm: '))
hov = float(input('Nhập số giờ tăng ca:'))
money = float(input('Nhập số tiền lương trả 1 giờ: '))
total = (h * 1 * money) + (hov * 1.5 * money)
print("Số tiền nhận là : ", total)






