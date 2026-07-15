# Functions :
def greet():
    """This function will greet everyone when it is called."""
    print("hey, have a great day!")
greet()

name = input("Enter your name: ")
def great(name):
    
    print("hey,",name,"have a great day!")
great(name)

def add(a, b):
    """Return the sum of two numbers."""
    return a + b
result = add(3, 5)  # This will return 8
print(result)  # This will print 8
help(add)








def greet():
    print("Hello")

greet()


def greet_user(name):
    print("Hello", name)

greet_user("Pavan")
greet_user("Rahul")


def add(a, b):
    return a + b

result = add(10, 20)
print(result)