#accept one no and print all even numbers till that number
def CalEven(No):

    lst = list()

    for i in range (1,No+1):
        if (i%2 == 0):
            lst.append(i)

    return lst


def main():
    n = int(input("Enter the Number :"))
    
    Ret = CalEven(n)
    
    print("Even numbers till ",n," are :",Ret)
if __name__ == "__main__":
    main()