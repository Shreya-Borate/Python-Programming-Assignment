'''Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

Input : Number of elements : 11

Input Elements : 13 5 45 7 4 56 5 34 2 5 65

Element to search : 5

Output : 3'''
def Display(List,freq):
    count = 0
    for i in List:
        if i == freq:
            count += 1
    return count
    

    
def main():
    lst = []
    n = int(input("Enter Number of elements : "))
    for i in range (n):
        numbers=int(input())
        lst.append(numbers)
    
    freqn = int(input("Element to search: "))

    Ret = Display(lst,freqn)
    print(f"Minimum Number is : {Ret} ")

if __name__ == "__main__":
    main()