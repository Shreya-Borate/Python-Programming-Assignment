#accpet one no and return sum of first N natural numbers.
def summation(No):
    result = 0
    for i in range (No+1):
        result += i
    return result


def main():
    n = int(input("Enter the number : "))
    Ret = summation(n)
    print("Sum of 1st atural numbers are : ",Ret)

if __name__=="__main__":
    main()