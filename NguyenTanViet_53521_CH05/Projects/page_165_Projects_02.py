"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: projects_01_page_165.py
Problem:
    Viết chương trình cho phép người dùng điều hướng các dòng văn bản trong tệp. Các
chương trình sẽ nhắc người dùng nhập tên tệp và nhập các dòng văn bản vào
danh sách. Sau đó, chương trình đi vào một vòng lặp trong đó nó in ra số dòng trong
và nhắc người dùng nhập số dòng. Số dòng thực nằm trong khoảng từ 1 đến
số dòng trong tệp. Nếu đầu vào là 0, chương trình sẽ thoát. Nếu không
chương trình in dòng liên kết với số đó

Solution:

Nhập tên tệp: enter_file
Số dòng trong txt này. tập tin là 2
Vui lòng nhập số dòng hoặc nhấn 0 để thoát: 1
tên tôi là khÃ¡ng

"""
enter_file = input("Nhập tên tệp: ")
file = open(enter_file, 'r')
line_count = 0

for line in file:
    line_count = line_count + 1

print("Số dòng trong txt này. tập tin là", line_count)

while True:
    line_num = 0

    num = int(input("Vui lòng nhập số dòng hoặc nhấn 0 để thoát: "))
    if 1 <= num <= line_count:
        file = open(enter_file, 'r')
        for lines in file:
            line_num = line_num + 1
            if line_num == num:
                print(lines)
    else:
        if num == 0:
            print("Cảm ơn vì đã sử dụng chương trình")
            break
