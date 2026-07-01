# check number divisible by 3 and 5
def ChkDivisibilty(No):
    if (No % 3 == 0) and (No % 5 == 0):
        return True

def main():
    n = int(input("Enter a number : "))
    Ret = ChkDivisibilty(n)
    
    if (Ret == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

if __name__ == "__main__":
    main()