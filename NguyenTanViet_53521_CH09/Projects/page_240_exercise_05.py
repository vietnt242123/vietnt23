"""
Author: NGUYEN TAN VIET
Date: 15/10/2021
Program: Projects_05_page_240.py

Problen:
   Xác định và kiểm tra một chức năng có tên là posterize. Hàm này mong đợi một hình ảnh
   và một bộ giá trị RGB làm đối số. Hàm sửa đổi hình ảnh như
   Hàm blackAndWhite, nhưng nó sử dụng các giá trị RGB đã cho thay vì màu đen.

Solution:

   Nhập tên tệp hình ảnh: Smokey.gif
   Nhập một số nguyên [0..255] cho màu đỏ: 0
   Nhập một số nguyên [0..255] cho màu xanh lục: 250
   Nhập một số nguyên [0..255] cho màu xanh lam: 0

"""

from images import Image


def posterize(image, color=(0, 0, 0)):
    """Chuyển đổi hình ảnh màu thành hai màu,
       một trong số đó màu trắng và một trong số đó là
       mặc định là màu đen hoặc do người dùng chỉ định
       Giá trị RGB."""

    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel(x, y, whitePixel)


def main():
    filename = input("Nhập tên tệp hình ảnh: ")
    red = int(input("Nhập một số nguyên [0..255] cho màu đỏ: "))
    green = int(input("Nhập một số nguyên [0..255] cho màu xanh lục: 250: "))
    blue = int(input("Nhập một số nguyên [0..255] cho màu xanh lam: "))
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()


main()

