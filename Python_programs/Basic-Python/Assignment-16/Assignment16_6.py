'''Write a program which accept number from user and check whether that number is positive or negative or zero.

Input : 11
Output : Positive Number

Input : -8
Output : Negative Number

Input : 0
Output : Zero'''
def NumChk(No):
    if No <=-1:
        print("Negative Number")
    elif No == 0:
        print("Zero")
    else:
        print("Positive Number")

def main():
    no = int(input("Enter a number : "))
    NumChk(no)
    

if __name__ == "__main__":
    main()