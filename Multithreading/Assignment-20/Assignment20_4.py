'''
Design a Python application that creates three threads named
Small, Capital and Digits.

All threads should accept a string as input.

Small thread:
- Count and display the number of lowercase characters.

Capital thread:
- Count and display the number of uppercase characters.

Digits thread:
- Count and display the number of numeric digits.

Each thread must also display:
- Thread ID
- Thread Name
'''

import threading

def Small(Str):
    Count = 0

    for ch in Str:
        if ch.islower():
            Count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small Letters :", Count)
    print()

def Capital(Str):
    Count = 0

    for ch in Str:
        if ch.isupper():
            Count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital Letters :", Count)
    print()

def Digits(Str):
    Count = 0

    for ch in Str:
        if ch.isdigit():
            Count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)
    print()

def main():
    String = input("Enter String : ")

    t1 = threading.Thread(target=Small, args=(String,), name="Small")
    t2 = threading.Thread(target=Capital, args=(String,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(String,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()