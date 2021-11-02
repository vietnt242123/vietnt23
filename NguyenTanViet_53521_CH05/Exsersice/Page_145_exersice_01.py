"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_01_page_145.py
Problem:
     Giả sử rằng dữ liệu biến tham chiếu đến danh sách [5, 3, 7]. Viết các giá trị của
                                   biểu thức sau:
a. data[2]
b. data[-1]
c. len(data)
d. data[0:2]
e. 0 in data
f. data + [2, 10, 5]
g. tuple(data)

Solution:

 Result the output:
a. 7
b. 7
c. 3
d. [5, 3]
e. False
f. [5, 3, 7, 2, 10, 5]
g. (5, 3, 7)

"""
data = [5, 3, 7]
# A
print(data[2])
# B
print(data[-1])
# C
print(len(data))
# D
print(data[0:2])
# E
print(0 in data)
# F
print(data + [2, 10, 5])
# G
print(tuple(data))
