#Program that accets one number and returns sum of that number.

def SumCal(No):
    sum = 0
    while No>0:
        digit = No%10
        sum += digit
        No=No//10
    return sum

def main():
    n = int(input("Enter number : "))
    Ret = SumCal(n)
    
    print("Digit count is :",Ret)

if __name__ == "__main__":
    main()