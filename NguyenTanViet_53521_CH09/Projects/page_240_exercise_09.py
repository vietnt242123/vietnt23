"""
Author: NGUYEN TAN VIET
Date: 16/10/2021
Program: Projects_01_page_145.py

Problen:

 Làm sáng và tối thực sự là những trường hợp đặc biệt của một quá trình được gọi là màu
sự lọc. Bộ lọc màu là bộ ba RGB bất kỳ được áp dụng cho toàn bộ hình ảnh. Bộ lọc
thuật toán điều chỉnh từng pixel theo số lượng được chỉ định trong bộ ba. Ví dụ,
bạn có thể tăng lượng màu đỏ trong hình ảnh bằng cách áp dụng bộ lọc màu với
giá trị dương màu đỏ và các giá trị xanh lục và xanh lam bằng 0. Bộ lọc (20, 0, 0) sẽ làm cho
màu tổng thể của hình ảnh hơi đỏ hơn. Ngoài ra, bạn có thể giảm số lượng
màu đỏ bằng cách áp dụng bộ lọc màu có giá trị âm màu đỏ. Một lần nữa, các thuật toán phải tránh vượt quá
các giới hạn về giá trị RGB.Phát triển ba thuật toán để làm sáng, làm tối và lọc màu làm ba
các chức năng Python liên quan, làm sáng, làm tối và colorFilter. Hai cái đầu tiên
các hàm nên mong đợi một hình ảnh và một số nguyên dương làm đối số

Solution:

Nhập tên tệp hình ảnh: dog.gif

"""
from images import Image


def colorFilter(image, rgbTriple):

    """Thêm các giá trị rgb đã cho vào mỗi pixel sau khi chuẩn hóa."""

    def baseValue(value, offset):

        """Bình thường hóa giá trị để 0 <= value <= 255."""
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = baseValue(r, rgbTriple[0])
            g = baseValue(g, rgbTriple[1])
            b = baseValue(b, rgbTriple[2])
            image.setPixel(x, y, (r, g, b))


def lighten(image, amount):
    """Làm sáng hình ảnh theo lượng."""
    colorFilter(image, (amount, amount, amount))


def darken(image, amount):
    """Làm đậm hình ảnh theo số lượng."""
    colorFilter(image, (-amount, -amount, -amount))


def main():
    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    print("Đóng cửa sổ để xem các thay đổi đối với hình ảnh")
    image.draw()
    lighten(image, 20)
    # darken(image, 20)
    image.draw()


main()
