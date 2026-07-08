'''
Design a Python application that creates two threads.

Thread 1 should compute the sum of elements from a list.

Thread 2 should compute the product of elements from the same list.

Return the results to the main thread and display them.
'''

import threading

SumResult = 0
ProductResult = 1

def SumList(List):
    global SumResult

    SumResult = sum(List)

def ProductList(List):
    global ProductResult

    ProductResult = 1

    for i in List:
        ProductResult *= i

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter elements :")
    for i in range(size):
        Data.append(int(input()))

    t1 = threading.Thread(target=SumList, args=(Data,))
    t2 = threading.Thread(target=ProductList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of Elements :", SumResult)
    print("Product of Elements :", ProductResult)

if __name__ == "__main__":
    main()