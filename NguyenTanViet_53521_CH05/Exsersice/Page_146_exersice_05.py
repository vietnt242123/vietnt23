"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_05_page_146.py
Problem:
    Giả sử rằng dữ liệu đề cập đến một danh sách các số và kết quả đề cập đến một danh sách trống.
    Viết một vòng lặp để thêm các giá trị khác không trong dữ liệu vào danh sách kết quả, giữ chúng
    ở các vị trí tương đối của chúng và loại trừ các số không

Solution:


"""

list = [1, 4, -5, 8]
result = []
index = 0
while index < list(list):
    list[index] = abs(list[index])
    index += 1
    result.append(list)
print(result)


