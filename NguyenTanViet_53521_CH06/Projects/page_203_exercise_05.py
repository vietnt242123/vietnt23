"""
Author: NGUYEN TAN VIET
Date: 24/010/2021
Program: page_203_project_05.py

Problem:

     A list is sorted in ascending order if it is empty or each item except the last one is
     less than or equal to its successor. Define a predicate isSorted that expects a list
     as an argument and returns True if the list is sorted, or returns False otherwise.

Solution:

True
False


"""
def isSorted(myList):

    """
    :param myList: enter a list
    :return: returns True if the list is sorted, or returns False otherwise.
    """
    if len(myList) == 0 or len(myList) == 1:
        return True
    else:
        for i in range(len(myList)):
            if myList[i] > myList[i + 1]:
                return False
    return True


def main():
    myList = []
    print(isSorted(myList))
    myList = [2, 1, 4]
    print(isSorted(myList))


if __name__ == '__main__':
    main()