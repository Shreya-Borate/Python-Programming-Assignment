'''Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

Input : Number of elements : 4

Input Elements : 13 5 45 7

Output : 5'''

def Display(List):
    mini = List[0]
    for i in List:
        if i < mini:
            mini = i        

    return mini

    
def main():
    lst = []
    n = int(input("Enter Number of elements : "))
    for i in range (n):
        numbers=int(input())
        lst.append(numbers)

    Ret = Display(lst)
    print(f"Minimum Number is : {Ret} ")

if __name__ == "__main__":
    main()