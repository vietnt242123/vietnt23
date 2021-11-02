"""
Author: NGUYEN TAN VIET
Date: 24/010/2021
Program: page_204_project_09.py

Problem:
    Problem:Program: Write a program that computes and prints the average of the numbers in a text
    file. You should make use of two higher-order functions to simplify the design.

Solution:
    Enter the file name: textnumber.txt
    The average is 3.0

"""

def main():

    fileName = input("Enter the file name: ")
    total = 0
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            for num in line.strip().split():
                total += float(num)
                count += 1
        print("\nThe average is " + str(total / count))


if __name__ == '__main__':
    main()