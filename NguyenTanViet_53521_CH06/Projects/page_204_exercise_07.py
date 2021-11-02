"""
Author: NGUYEN TAN VIET
Date: 24/010/2021
Program: page_204_project_07.py

Problem:

 Problem:Program: Write a recursive function that expects a pathname as an argument. The pathname can be either the name of
 a file or the name of a directory. If the pathname refers to a file, its name is displayed, followed by its contents.
 Otherwise, if the pathname refers to a directory, the function is applied to each name in the directory.
 Test this function in a new program

Solution:

"""
import os


def displayFiles(pathname):
    """
    :param pathname: pathname can be either the name of
    a file or the name of a directory
    :return: display a file
    """
    # if parameter is pathname for directory
    if os.path.isdir(pathname):
        # open the directory
        for i in os.listdir(pathname):
            # mark items in list
            newItem = os.path.join(pathname, i)
            # print each file name
            # call the function recurse
            displayFiles(newItem)
    # if the pathname is file name
    else:
        # set the pathname to filename
        filename = pathname
        baseFile = os.path.basename(filename)
        print(f"File name: {baseFile}")
        # open the file in read mode
        with open(filename, "r") as file:
            print("Content: ")
            # display the contents of the file
            for line in file:
                print(line)
            print()


displayFiles("page_203_exercise_01.py")