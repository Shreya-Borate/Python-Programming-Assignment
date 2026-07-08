'''
Design a Python application that creates two threads named Prime and NonPrime.

Both threads should accept a list of integers.

The Prime thread should display all prime numbers from the list.

The NonPrime thread should display all non-prime numbers from the list.
'''

import threading

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def Prime(List):
    print("Prime Numbers :")
    for i in List:
        if ChkPrime(i):
            print(i, end=" ")
    print()

def NonPrime(List):
    print("Non Prime Numbers :")
    for i in List:
        if not ChkPrime(i):
            print(i, end=" ")
    print()

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter elements :")
    for i in range(size):
        Data.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()