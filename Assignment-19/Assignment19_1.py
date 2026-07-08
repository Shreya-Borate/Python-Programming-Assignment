'''Write a program which contains one lambda function which accepts one parameter and return power of two.

Input : 4
Output : 16

Input : 6
Output : 64'''
Power = lambda No : No*2


def main():
    n = int(input("Enter Number : "))
    
    Ret = Power(n)

    print(Ret)


if __name__ == "__main__":
    main()