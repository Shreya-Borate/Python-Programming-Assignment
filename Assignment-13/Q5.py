# Program to accept marks and display grade

def DisplayGrade(Marks):
    if Marks >= 75:
        return "Distinction"
    elif Marks >= 60:
        return "First Class"
    elif Marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    Marks = float(input("Enter marks: "))

    Ret = DisplayGrade(Marks)

    print("Grade:", Ret)


if __name__ == "__main__":
    main()