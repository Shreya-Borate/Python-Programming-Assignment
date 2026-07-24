'''Write a Python program which accepts two file names through command line arguments and compares the contents of both files.

• If both files contain the same contents, display Success.

• Otherwise display Failure.

Input (Command Line):
Demo.txt Hello.txt

Expected Output:
Success OR Failure'''

import sys

file1 = open(sys.argv[1], "r")
file2 = open(sys.argv[2], "r")

data1 = file1.read()
data2 = file2.read()

file1.close()
file2.close()

if data1 == data2:
    print("Success")
else:
    print("Failure")