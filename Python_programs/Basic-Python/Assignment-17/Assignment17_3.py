'''Write a program which accept one number from user and return its factorial.

Input : 5
Output : 120'''
def Display(No):
    fact = 1
    for i in range (1,No+1):
        fact *=i
    return fact


def main():
    n = int (input("Enter Number : "))
    Ret = Display(n)
    print(Ret)
    

if __name__ == "__main__":
    main()