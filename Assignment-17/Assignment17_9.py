'''Write a program which accept number from user and return number of digits in that number.

Input : 5187934
Output : 7'''
def Display(No):
    count = 0
    while No > 0:
        count +=1
        No = No//10
    return count


def main():
    n = int (input("Enter Number : "))
    Ret = Display(n)
    print(Ret)
    

if __name__ == "__main__":
    main()