'''3.

Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

Input List =

[4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

List after filter =

[76, 89, 86, 90, 70]

List after map =

[86, 99, 96, 100, 80]

Output of reduce =

6538752000'''
from functools import reduce

FilterX = lambda No : (No >= 70) and (No <= 90)
MapX = lambda No : No + 10
ReduceX = lambda A, B : A * B

def main():

    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter elements :")
    for i in range(size):
        value = int(input())
        Data.append(value)

    FData = list(filter(FilterX, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    RData = reduce(ReduceX, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()