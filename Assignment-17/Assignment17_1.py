'''Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.'''


from Arithmetic import *

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    print("Addition :", Add(value1, value2))
    print("Subtraction :", Sub(value1, value2))
    print("Multiplication :", Mult(value1, value2))
    print("Division :", Div(value1, value2))

if __name__ == "__main__":
    main()