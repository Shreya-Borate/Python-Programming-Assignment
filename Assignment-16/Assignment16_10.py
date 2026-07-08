'''Write a program which accept name from user and display length of its name.

Input : Marvellous
Output : 10'''

def CalLen(w):
    Len = len(w)
    print(Len)

def main():
    Str = input("Enter name : ")
    CalLen(Str)
    

if __name__ == "__main__":
    main()