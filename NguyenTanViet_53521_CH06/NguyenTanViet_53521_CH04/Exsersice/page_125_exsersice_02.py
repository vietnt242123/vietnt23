"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_02_page_125.py
Problem:
       Viết một đoạn mã để mở một tệp để nhập và in ra số
               các từ gồm bốn chữ cái trong tệp
Solution:

"""
filename = input('Nhập tên của tệp: ')
file = open(filename, 'a')
file1 = open(filename, 'b')
i = 0
for element in file:
    words = element.split()
    for i in range(len(words)):
        file1 = element.replaca(i, 'xxxx')
        i = i + 1
file.close()





