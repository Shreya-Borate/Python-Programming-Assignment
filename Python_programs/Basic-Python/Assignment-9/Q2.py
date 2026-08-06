#check greater number between given two numbers
def ChkGreater(No1,No2):
    if (No1 > No2):
        return True
    else:
        return False

def main():
    value1 = 10
    value2 = 20

    Ret = ChkGreater(value1,value2)

    if (Ret == True):
        print("Greater value is : ",value1)
    else:
        print("Greater value is : ",value2)

if __name__ == "__main__":
    main()