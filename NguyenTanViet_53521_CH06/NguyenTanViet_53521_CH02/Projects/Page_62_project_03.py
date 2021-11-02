"""
Author: NGUYEN TAN VIET
Date: 03/09/2021
Program: page_62_project_03.py
Problem:
     Five Star Retro Video cho thuê băng VHS và DVD cho những người sành sỏi
     thích mua các album ghi âm LP. Cửa hàng cho thuê các video mới với giá $ 3,00 một đêm và
     đồ cũ với giá $ 2,00 một đêm. Viết một chương trình mà nhân viên bán hàng tại Five Star Retro Video
     có thể sử dụng để tính tổng chi phí cho việc thuê video của khách hàng. Chương trình
     sẽ nhắc người dùng về số lượng từng loại video và xuất ra tổng số
     Giá cả

Solution:

"""
a = int(input('Mời nhập số lượng băng đĩa mới: '))
b = int(input('Mời nhập số lượng băng đĩa cũ: '))
d = int(input('Mời nhập số ngày thuê: '))
money = (a * d * 3) + (b * d * 2)
print("Tổng số tiền là:  ", money, "$")

