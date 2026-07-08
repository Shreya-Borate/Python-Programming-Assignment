'''
Design a Python application that creates two threads.

Thread 1 should calculate and display the maximum element from a list.

Thread 2 should calculate and display the minimum element from the same list.

The list should be accepted from the user.
'''

import threading

def Maximum(List):
    print("Maximum Element :", max(List))

def Minimum(List):
    print("Minimum Element :", min(List))

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter elements :")
    for i in range(size):
        Data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()