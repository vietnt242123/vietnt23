"""
Author: Nguyen Tan Viet
Date: 15/09/2021
Program: Project_05_page_100.py
Problem:
        Một nhà sinh vật học địa phương cần một chương trình để dự đoán sự gia tăng dân số. Các đầu vào
sẽ là số lượng sinh vật ban đầu, tốc độ phát triển (một số thực
lớn hơn 0), số giờ cần để đạt được tốc độ này và một số
số giờ trong đó dân số tăng lên. Ví dụ: một người có thể bắt đầu bằng
quần thể 500 sinh vật, tốc độ tăng trưởng là 2 và thời kỳ tăng trưởng cần đạt được
tỷ lệ này trong 6 giờ. Giả sử rằng không có sinh vật nào chết, điều này có nghĩa là
rằng dân số này sẽ tăng gấp đôi sau mỗi 6 giờ. Vì vậy, sau khi cho phép
6 giờ để tăng trưởng, chúng tôi sẽ có 1000 sinh vật và sau 12 giờ, chúng tôi sẽ
có 2000 sinh vật. Viết một chương trình lấy các đầu vào này và hiển thị dự đoán về tổng dân số.
Solution:

"""
organisms = int(input("Enter the initial number of organisms:"))
rateOfGrowth = int(input("Enter the rate of growth [a real number > 0]: "))
numOfHours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalHours = int(input("Enter the total hours of growth: "))
totalOrganisms = organisms * rateOfGrowth * 2
while numOfHours >= totalHours:
    organisms *= rateOfGrowth
    totalOrganisms += organisms
    numOfHours += numOfHours
print("The total population is ", totalOrganisms)


