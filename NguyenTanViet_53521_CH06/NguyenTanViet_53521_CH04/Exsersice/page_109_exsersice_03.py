"""
Author: Nguyen Tan Viet
Date: 28/09/2021
Program: exersice_03_page_109.py
Problem:
        Bạn được cung cấp một chuỗi được mã hóa bằng mật mã Caesar với giá trị khoảng cách không xác định.
        Văn bản có thể chứa bất kỳ ký tự ASCII nào có thể in được. Đề xuất một thuật toán để bẻ khóa mã này.

Solution:

        Một sơ đồ mã hóa phức tạp hơn được gọi là mật mã khối.
        Mật mã khối sử dụng các ký tự bản rõ để tính hai hoặc nhiều ký tự mã hóa.
        Điều này được thực hiện bằng cách sử dụng một cấu trúc toán học được biết đến như một ma trận khả nghịch
        để xác định các giá trị của các ký tự được mã hóa. Ma trận cung cấp khóa trong phương pháp này.
        Máy thu sử dụng cùng một ma trậnđể giải mã văn bản mật mã.
        Thực tế là thông tin được sử dụng để xác định mỗi ký tự đến từ một khối dữ liệu
        khiến việc xác định khóa trở nên khó khăn hơn.
"""

