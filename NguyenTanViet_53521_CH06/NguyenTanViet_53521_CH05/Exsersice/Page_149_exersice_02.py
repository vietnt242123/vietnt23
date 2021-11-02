"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_02_page_149.py
Problem:
      Xác định một hàm có tên chẵn. Hàm này mong đợi một số làm đối số và
      trả về True nếu số chia hết cho 2 hoặc trả về False nếu ngược lại. (Gợi ý: A
                      số chia hết cho 2 nếu dư là 0.)
Solution:

"""
odd(5)
odd(6)
def odd(x):
    "trả về True nếu số chia hết cho 2 hoặc trả về False nếu ngược lại"
    if x % 2 == 1:
        return True
    else:
        return False
  print(odd(5))












