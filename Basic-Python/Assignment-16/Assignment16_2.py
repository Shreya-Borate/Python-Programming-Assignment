'''Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.

Input : 11
Output : Odd Number

Input : 8
Output : Even Number'''


def CheckEven(No):
    return (No % 2 == 0)

def main():
    value = int(input("Enter Number : "))

    Ret = CheckEven(value)

    if (Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")

if __name__ == "__main__":
    main()