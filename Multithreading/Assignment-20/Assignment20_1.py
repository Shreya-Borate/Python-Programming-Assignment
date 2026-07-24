'''
Design a Python application that creates two separate threads named Even and Odd.

The Even thread should display the first 10 even numbers.
The Odd thread should display the first 10 odd numbers.

Both threads should execute independently using the threading module.
Ensure proper thread creation and execution.
'''

import threading

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i, end=" ")
    print()

def main():
    t1 = threading.Thread(target=Even, name="Even")
    t2 = threading.Thread(target=Odd, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()