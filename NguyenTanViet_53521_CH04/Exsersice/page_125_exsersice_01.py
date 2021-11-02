"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_01_page_125.py
Problem:
        Viết một đoạn mã để mở một tệp có tên myfile.txt để nhập và in
                             số dòng trong tệp
Solution:

"""
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if line == '':
        break
    print(line)





