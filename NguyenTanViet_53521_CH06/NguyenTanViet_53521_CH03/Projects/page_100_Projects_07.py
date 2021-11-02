"""
Author: Nguyen Tan Viet
Date: 18/09/2021
Program: Project_07_page_100.py
Problem:
iáo viên ở hầu hết các khu học chánh được trả lương theo lịch trình
dựa trên số năm kinh nghiệm giảng dạy của họ. Ví dụ, một sự khởi đầu
giáo viên trong Học khu Lexington có thể được trả $ 30.000 trong năm đầu tiên. Vì
mỗi năm kinh nghiệm sau năm đầu tiên này, tối đa 10 năm, giáo viên nhận được
Tăng 2% so với giá trị trước đó. Viết một chương trình hiển thị một bảng lương, ở dạng bảng, cho giáo viên trong một khu học chánh. Các đầu vào là khởi đầu
lương, tỷ lệ phần trăm tăng và số năm trong lịch trình. Từng hàng
trong lịch trình phải có số năm và mức lương của năm đó

Solution:

"""
star_salary = int(input("Nhập số tiền khởi điểm: $"))
increa = 2 / 100
year = int(input("Nhập số năm làm việc"))
salary = star_salary
if year >= 1 and year <= 10:
    if year == 1:
        print(" Số lương của bạn : ", star_salary)
    else:
        print("Số lương của bạn: ", star_salary)
    for a in range(2, year + 1):
        salary = salary + salary * increa
        print(" Số lương của bạn là: ", a, salary)
