#program that accepts one number and return its binary equivalent
def DecimalToBinary(No):
    return bin(No)[2:]      # Remove '0b' prefix

def main():
    Num = int(input("Enter a number: "))

    Ret = DecimalToBinary(Num)

    print("Binary equivalent is:", Ret)

if __name__ == "__main__":
    main()