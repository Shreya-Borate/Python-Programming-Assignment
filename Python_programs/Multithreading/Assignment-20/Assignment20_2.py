'''
Design a Python application that creates two threads named EvenFactor and OddFactor.

Both threads should accept one integer number as a parameter.

EvenFactor thread:
- Identify all even factors of the given number.
- Calculate and display the sum of even factors.

OddFactor thread:
- Identify all odd factors of the given number.
- Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display:
"Exit from main"
'''

import threading

def EvenFactor(No):
    Sum = 0

    print("Even Factors:")
    for i in range(1, No + 1):
        if(No % i == 0 and i % 2 == 0):
            print(i, end=" ")
            Sum += i

    print("\nSum of Even Factors =", Sum)

def OddFactor(No):
    Sum = 0

    print("Odd Factors:")
    for i in range(1, No + 1):
        if(No % i == 0 and i % 2 != 0):
            print(i, end=" ")
            Sum += i

    print("\nSum of Odd Factors =", Sum)

def main():
    num = int(input("Enter Number : "))

    t1 = threading.Thread(target=EvenFactor, args=(num,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(num,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()