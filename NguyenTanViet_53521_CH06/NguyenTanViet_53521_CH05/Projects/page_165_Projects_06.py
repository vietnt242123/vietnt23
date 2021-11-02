"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: projects_01_page_165.py
Problem:
    Xác định một hàm decimalToRep trả về biểu diễn của một số nguyên trong một
cơ sở cho trước. Hai đối số phải là số nguyên và cơ số. Chức năng
sẽ trả về một chuỗi. Nó phải sử dụng một bảng tra cứu liên kết các số nguyên với
các chữ số. Bao gồm một chức năng chính kiểm tra chức năng chuyển đổi với các số
trong một số cơ sở.
Solution:


"""
repTable = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
            5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 14: 'D',
            15: 'E', 16: 'F'}

def decimalToRep(decimal, base):
    if decimal == 0:
        return '0'
    else:
        rep = ""
        while decimal > 0:
            remainder = decimal % base
            decimal = decimal // base
            rep = repTable[remainder] + rep
        return rep



def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))


if __name__ == '__main__':
    main()



