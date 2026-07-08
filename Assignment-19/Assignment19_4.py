'''Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

Input List =

[5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

List after filter =

[2, 4, 4, 2, 8, 10]

List after map =

[4, 16, 16, 4, 64, 100]

Output of reduce =

204'''

from functools import reduce

FilterX = lambda No : (No % 2 == 0)
MapX = lambda No : No * No
ReduceX = lambda A, B : A + B

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