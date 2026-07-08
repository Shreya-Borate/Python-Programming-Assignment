'''
Design a Python application that creates two threads named EvenList and OddList.

Both threads should accept a list of integers as input.

EvenList thread:
- Extract all even elements from the list.
- Calculate and display their sum.

OddList thread:
- Extract all odd elements from the list.
- Calculate and display their sum.

Threads should run concurrently.
'''

import threading

def EvenList(Data):
    Sum = 0

    for i in Data:
        if(i % 2 == 0):
            Sum += i

    print("Sum of Even Numbers :", Sum)

def OddList(Data):
    Sum = 0

    for i in Data:
        if(i % 2 != 0):
            Sum += i

    print("Sum of Odd Numbers :", Sum)

def main():

    List = []

    size = int(input("Enter Number of Elements : "))

    print("Enter Elements :")

    for i in range(size):
        value = int(input())
        List.append(value)

    t1 = threading.Thread(target=EvenList, args=(List,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(List,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()