#accept one no and print all odd numbers till that number
def CalOdd(No):

    lst = list()

    for i in range (1,No+1):
        if (i%2 == 0):
            continue
        else:
            lst.append(i)

    return lst


def main():
    n = int(input("Enter the Number :"))
    
    Ret = CalOdd(n)
    
    print("Even numbers till ",n," are :",Ret)
if __name__ == "__main__":
    main()