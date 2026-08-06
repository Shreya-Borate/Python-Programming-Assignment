'''• The class should contain two instance variables: Value1 and Value2.

• Define a constructor (__init__) that initializes all instance variables to 0.

• Implement the following instance methods:
    o Accept() – accepts values for Value1 and Value2 from the user.
    o Addition() – returns the addition of Value1 and Value2.
    o Subtraction() – returns the subtraction of Value1 and Value2.
    o Multiplication() – returns the multiplication of Value1 and Value2.
    o Division() – returns the division of Value1 and Value2 (handle division by zero properly).

• Create multiple objects of the Arithmetic class and invoke all the instance methods.'''

class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter value 1 : "))
        self.Value2 = int(input("Enter value 2 : "))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    

obj1 = Arithmatic()
obj2 = Arithmatic()

print("Enter Value for obj1 : ")
obj1.Accept()
print("Addition =", obj1.Addition())
print("Subtraction =", obj1.Subtraction())
print("Multiplication =", obj1.Multiplication())
print("Division =", obj1.Division())
print()
print("Enter Value for obj2 : ")
obj2.Accept()
print("Addition =", obj2.Addition())
print("Subtraction =", obj2.Subtraction())
print("Multiplication =", obj2.Multiplication())
print("Division =", obj2.Division())
    