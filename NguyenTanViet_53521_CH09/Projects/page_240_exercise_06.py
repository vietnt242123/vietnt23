"""
Author: NGUYEN TAN VIET
Date: 15/10/2021
Program: Projects_06_page_240.py

Problen:

    Xác định phiên bản thứ hai của hàm thang độ xám sử dụng hàm bị cáo buộc là thô
    phương pháp lấy trung bình đơn giản từng giá trị RGB. Kiểm tra chức năng bằng cách so sánh
    kết quả với những kết quả của phiên bản khác được thảo luận trong chương này.

Solution:

    Nhập tên tệp hình ảnh: dog.gif

"""
from images import Image


def grayscale1(image):
    """Chuyển đổi hình ảnh sang thang độ xám bằng cách sử dụng
       biến đổi tâm lý chính xác."""

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


def grayscale2(image):
    """Chuyển đổi hình ảnh sang thang độ xám bằng cách sử dụng mức trung bình thô
       trong số r, g và b"""

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            ave = (r + g + b) // 3
            image.setPixel(x, y, (ave, ave, ave))


if __name__ == '__main__':
    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    grayscale2(image)
    image.draw()
