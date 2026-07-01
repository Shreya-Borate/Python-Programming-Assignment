#accept one number and print count of digits in that number.
def DigitCal(No):
    count = 0
    while No >0:
        count +=1
        No = No//10

    return count


def main():
    n = int(input("Enter number : "))
    Ret = DigitCal(n)
    
    print("Digit count is :",Ret)

if __name__ == "__main__":
    main()