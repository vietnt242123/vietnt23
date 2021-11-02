"""
Program: page_73_casestydy_01.py
Author: Nguyen Tan Viet
Date: 18/09/2021
       Compute an investment report.
  1. The inputs are
         starting investment amount
         number of years
         interest rate (an integer percent)
  2. The report is displayed in tabular form with a header.
  3. Computations and outputs:
         for each year
         compute the interest and add it to the investment
         print a formatted row of results for that year
  4. The ending investment and interest earned are also
         displayed.
"""
# Chấp nhận đầu vào

startBalance = float(input("Nhập số tiền đầu tư: "))
years = int(input("Nhập số năm: "))
rate = int(input("Nhập tỷ lệ dưới dạng a %: "))

# Chuyển đổi tỷ lệ thành số thập phân
rate = rate / 100

# Khởi tạo bộ tích lũy cho lãi suất

totalInterest = 0.0

# Hiển thị tiêu đề cho bảng

print("%4s%18s%10s%16s" % \
      ("Year", "Starting balance",
     "Interest", "Ending balance"))

# Tính toán và hiển thị kết quả cho mỗi năm

for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % \
    (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest

