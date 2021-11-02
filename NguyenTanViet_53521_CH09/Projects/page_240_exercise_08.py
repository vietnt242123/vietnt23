"""
Author: NGUYEN TAN VIET
Date: 16/10/2021
Program: Projects_01_page_145.py
Problen:
 Những bức ảnh kiểu cũ từ thế kỷ 19 không hoàn toàn đen và
màu trắng và không hoàn toàn là màu, nhưng dường như có các sắc thái xám, nâu và xanh lam. Cái này
hiệu ứng được gọi là nâu đỏ,
Viết và kiểm tra một chức năng có tên là sepia để chuyển đổi hình ảnh màu thành màu nâu đỏ. Cái này
trước tiên hàm nên gọi thang độ xám để chuyển đổi hình ảnh màu sang thang độ xám. MỘT
đoạn mã để chuyển đổi các giá trị thang độ xám để đạt được hiệu ứng màu nâu đỏ như sau.

Solution:

Nhập tên tệp hình ảnh: dog.gif

"""
from images import Image


def sepia(image):
    """Chuyển đổi hình ảnh sang màu nâu đỏ."""
    grayscale(image)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            image.setPixel(x, y, (r, g, b))


def grayscale(image):
    """Chuyển đổi hình ảnh sang thang độ xám."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


if __name__ == '__main__':

    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    sepia(image)
    image.draw()