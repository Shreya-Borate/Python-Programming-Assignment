#Check palindrome
def ChkPalindrome(No):
    return (No == No[::-1])
    


def main():
    n=input("Enter a number : ")
    Ret = ChkPalindrome(n)

    if (Ret==True) :
        print("The Number is palindrome ")
    else:
        print("The Number is  not palindrome ")

if __name__ =="__main__":
    main()