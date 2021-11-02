"""
Author: NGUYEN TAN VIET
Date: 16/10/2021
Program: Projects_07_page_240.py

Problen:
   Đảo ngược một hình ảnh làm cho nó trông giống như một bức ảnh âm bản. Xác định và kiểm tra
   một chức năng có tên là invert. Hàm này mong đợi một hình ảnh làm đối số và
   đặt lại mỗi thành phần RGB thành 255 trừ đi thành phần đó. Hãy chắc chắn để kiểm tra
   chức năng với hình ảnh đã được chuyển đổi sang thang độ xám và đen trắng
   cũng như hình ảnh màu

Solution:

   Nhập tên tệp hình ảnh: dog.gif

"""
from images import Image


def invert(image):
    """Đảo ngược một hình ảnh thành âm bản của nó."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            image.setPixel(x, y, (255 - r, 255 - g, 255 - b))


def blackAndWhite(image):

    """Chuyển đổi hình ảnh thành đen trắng."""

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)


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
    grayscale(image)
    invert(image)
    image.draw()
