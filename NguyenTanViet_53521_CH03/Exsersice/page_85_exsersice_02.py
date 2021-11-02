"""
Author: Nguyen Tan Viet
Date: 08/09/2021
Program: exersice_02_page_85.py
Problem:
        Giả sử rằng x đề cập đến một số. Viết một phân đoạn mã in số
        giá trị tuyệt đối mà không cần sử dụng chức năng abs của Python
Solution:

"""
def myabs(n):
    if (n<0):
        return n *- 1
print(myabs(-10))
print(myabs(10))