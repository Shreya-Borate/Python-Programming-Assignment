'''Write a program which contains one lambda function which accepts two parameters and return its multiplication.

Input : 4 3
Output : 12

Input : 6 3
Output : 18'''

Mul = lambda No1,No2 : No1 * No2


def main():
    n1 = int(input("Enter 1st Number  : "))
    n2 = int(input("Enter 2nd Number  : "))
    
    Ret = Mul(n1,n2)

    print(Ret)


if __name__ == "__main__":
    main()