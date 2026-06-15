#Q2 What is the difference between: a=10 b=10 and a= [10] b= [10] explain using id()
a = 10
b = 10

print(id(a))
print(id(b))

a = [10]
b = [10]

print(id(a))
print(id(b))