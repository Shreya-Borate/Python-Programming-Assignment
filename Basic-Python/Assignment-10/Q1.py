# accpet one no and return multiplication table of that number.
def Multi(No):
    for i in range (1,11):
        result = No*i
        print(result)


def main():
    n = int(input("Enter a number : "))
    Ret = Multi(n)
    

if __name__== "__main__":
    main()