#factorial of number
def Fact(No):
    Fact=1
    for i in range (1,No+1):
        Fact *=i
    return Fact


def main():
    n=int(input("Enter the number : "))
    Ret = Fact(n)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()