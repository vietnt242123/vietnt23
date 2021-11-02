"""
DE: 01
Author: CA20B1_53521_NguyenTanViet
Date: 01/10/2021

Problem:
      Câu 1 (2.0 điểm). Viết hàm in các số nguyên tố trong khoảng từ 30 đến 200

Solution:

"""
def Cau1():
    def snt(n):
        """ Check so nguyen to """
        f = True
        for j in range(2, n):
            if n % j == 0:
                f = False
                break
        return f

    def in_snt(a=30, b=200):
        print("Danh sach so nguyen to:")
        """Kiem tra so nguyen to trong khoang tu a den b"""
        for i in range(a, b + 1):
            if snt(i):
                print(i, end="  ")
        print()

    # thực thi tim số nguyên tố
    in_snt(30, 200)


if __name__ == '__main__':
    Cau1()







