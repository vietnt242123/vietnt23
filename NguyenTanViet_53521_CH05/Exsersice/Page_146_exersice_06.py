"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_06_page_146.py
Problem:
    Viết một vòng lặp thay thế mỗi số trong danh sách có tên dữ liệu bằng giá trị tuyệt đối của nó
Solution:

"""
# khởi tạo danh sách
test_list = [2, 5, 4, -9, -7]

# in danh sách gốc
print("Danh sách ban đầu là: " + str(test_list))

# sử dụng abs () + đọc hiểu danh sách
rts = [abs(ele) for ele in test_list]

# kết quả in
print("Danh sách giá trị tuyệt đối: " + str(res))

