"""
Author: Nguyen Tan Viet
Date: 15/09/2021
Program: Project_04_page_92.py
Problem:
        Một thí nghiệm khoa học tiêu chuẩn là thả một quả bóng và xem nó nảy lên cao đến mức nào.
        Khi “độ nảy” của quả bóng đã được xác định, tỷ số này sẽ đưa ra chỉ số bounci ness.
        Ví dụ, nếu một quả bóng rơi từ độ cao 10 feet sẽ nảy lên 6 feet
        cao, chỉ số 0,6 và tổng quãng đường bóng đi được là 16 feet sau
        một lần trả lại. Nếu quả bóng tiếp tục nảy thì khoảng cách sau hai lần nảy
        sẽ là 10 ft 6 111 ft 6 ft 3,6 ft 5 25,6 ft. Lưu ý rằng khoảng cách di chuyển cho
        mỗi lần trả lại liên tiếp là khoảng cách đến sàn cộng với 0,6 của khoảng cách đó là
        bóng quay trở lại. Viết chương trình cho phép người dùng nhập chiều cao ban đầu
        từ đó thả bóng và số lần thả bóng tiếp tục nảy.
        Đầu ra phải là tổng quãng đường bóng đi được.
Solution:

"""
height = float(input("nhập chiều cao ban đầu (in feet): "))
bounces = int(input("nhập số lần bounces: "))
bouciness = 0.6
total = 0
while bounces > 0:
    total = total + height
    height = height * bouciness
    total = total + height
    bounces -= 1
print("tổng quãng đường bóng đi được là: ", total)



