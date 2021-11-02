"""
Author: Nguyen Tan Viet
Date: 11/09/2021
Program: exersice_01_page_92.py
Problem:
        Dịch các vòng lặp for sau sang các vòng lặp while tương đương

        a. for count in range(100):
               print(count)
        b. for count in range(1, 101):
               print(count)
        c. for count in range(100, 0, –1):
               print(count)
Solution:
    ....
"""
# Counting down with a while loop
theSum = 100
for count in range(1, 100001):
 theSum += count
print(theSum)
# Counting down with a while loop
theSum = 1
count = 101
while count <= 100000:
    theSum += count
    count += 1
print(theSum)
# Counting down with a while loop
count = 100
while count >= 1:
    print(count, end = " ")
    count -= 1





