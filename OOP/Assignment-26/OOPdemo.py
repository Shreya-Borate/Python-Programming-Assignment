'''Q1. Write a Python program to implement a class named Demo with the following specifications:

• The class should contain two instance variables: no1 and no2.

• The class should contain one class variable named Value.

• Define a constructor (__init__) that accepts two parameters and initializes the instance variables.

• Implement two instance methods:
  o Fun() – displays the values of instance variables no1 and no2.
  o Gun() – displays the values of instance variables no1 and no2.

Create two objects of the Demo class as follows:

Obj1 = Demo(11, 21)

Obj2 = Demo(51, 101)

Call the instance methods in the given sequence:

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()'''

class Demo:
    #class variable
    value =  10
    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    #Instance method 1
    def Fun(self):
        print("Inside Fun method")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

    #Instance method 1
    def Gun(self):
        print("Inside Gun method")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()      #11,21
obj2.Fun()      #51,101
obj1.Gun()      #11,21
obj2.Gun()      #51,101
