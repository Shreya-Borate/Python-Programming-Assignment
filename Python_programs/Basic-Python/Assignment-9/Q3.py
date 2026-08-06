# program that accepts one number and return its square

def SquareNo(No):
    result = No*2
    return result
def main():
    n = int(input("Enter One number : "))
    Ret = SquareNo(n)
    print("Square of number is : ",Ret)

if __name__ == "__main__":
    main()