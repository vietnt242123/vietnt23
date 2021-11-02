"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_02_page_145.py
Problem:
      Giả sử rằng dữ liệu biến tham chiếu đến danh sách [5, 3, 7]. Viết các biểu thức
                               thực hiện các tác vụ sau:
    a. Replace the value at position 0 in data with that value’s negation.
    b. Add the value 10 to the end of data.
    c. Insert the value 22 at position 2 in data.
    d. Remove the value at position 1 in data.
    e. Add the values in the list newData to the end of data.
    f. Locate the index of the value 7 in data, safely.
    g. Sort the values in data.

Solution:

    a. data[0] = -data[0]
Result: [-5, 3, 7]
    b. data.append(10)
Result: [-5, 3, 7, 10]
    c. data.insert(2, 22)
Result: [-5, 3, 22, 7, 10]
    d. del data[1]
Result: [-5, 22, 7, 10]
    e.  newData = [2, 8]
data + newData
Result: [-5, 22, 7, 10, 2, 8]
    f. data[2]
Result: 7
    g. data.sort()
Result: [-5, 22, 7, 10]

"""