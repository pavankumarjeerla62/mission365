# ==========================================================
# Python Functions Practice - Day 2
# Topic: Functions, Parameters, Arguments, Return & Scope
#
# These are my practice programs while learning Python.
# I have intentionally tried different examples to understand
# how functions work internally.
# ==========================================================


# ----------------------------------------------------------
# Simple function without parameters
# A function is a reusable block of code.
# It only runs when we call it using ().
# ----------------------------------------------------------

def greet():
    print("hello")

greet()

print("pavan")

# Printing the function name without ()
# prints the function object, not its output.
print(greet)


# ----------------------------------------------------------
# Program Flow
# Python executes statements from top to bottom.
# Whenever a function is called, Python jumps into it,
# executes it, and then comes back.
# ----------------------------------------------------------

def greet():
    print("hello")

print("start")

greet()

print("stop")

greet()


# ----------------------------------------------------------
# Parameters & Arguments
#
# Parameter -> variable inside function definition.
# Argument  -> actual value passed while calling.
# ----------------------------------------------------------

def greet(name):
    print(" hello well come",name)

greet("Pavan")
greet("rahul")
greet("kjdhd")


# ----------------------------------------------------------
# User Input + Function
#
# Here I am taking input from the user and creating
# an add() function.
#
# Note:
# In this example I passed fixed values (5,9)
# instead of the user inputs just for practice.
# ----------------------------------------------------------

a= int(input("enter the values for a : "))
b = int(input("enter the values for b : "))

def add(a,b):
    c = a+b
    return c

add(5,9)


# ----------------------------------------------------------
# Multiple Parameters
#
# A function can receive more than one value.
# Python assigns arguments to parameters
# in the same order.
# ----------------------------------------------------------

def greet(name,city,age):
    print(" hello wellcome",name, "your  from", city ,"your",age,"years old so you can vote")

greet("Pavan","hyd", 21)
greet("rahul","usa","21")


# ----------------------------------------------------------
# Taking user input and passing it to the function.
#
# Instead of hardcoding values,
# we are collecting values from the user.
# ----------------------------------------------------------

name = input("enter the name: ")
city = input("enter the city: ")
age =int(input("enter the age: "))

def greet(name,city,age):

    print(" hello wellcome",name, "your  from", city ,"your",age,"years old so you can vote")

greet(name,city,age)


# ----------------------------------------------------------
# print() vs return()
#
# print() only displays the value.
# It DOES NOT send anything back.
# Therefore result becomes None.
# ----------------------------------------------------------

def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)


# ----------------------------------------------------------
# return sends the value back to the caller.
# Now the returned value is stored inside result.
# ----------------------------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# Since result contains 30,
# we can reuse it for another calculation.

last=result*10

print(last)


# ----------------------------------------------------------
# Simple example of return.
# The function returns a value.
# ----------------------------------------------------------

def get_followers():
    return 1250

followers = get_followers()

print(followers)


# ----------------------------------------------------------
# Returned value can also be used in conditions.
# Here the returned followers count
# is checked using if statement.
# ----------------------------------------------------------

def get_followers():
    return 1250

followers = get_followers()

if followers > 1000:
    print("Popular Account")


# ----------------------------------------------------------
# Function Chaining
#
# One function returns a value.
# That returned value becomes the input
# of another function.
# ----------------------------------------------------------

def add(a, b):
    return a + b

def square(number):
    return number * number

result = square(add(2, 3))

print(result)


# ----------------------------------------------------------
# Again checking print() vs return().
#
# add() prints the answer,
# but returns None.
# ----------------------------------------------------------

def add(a, b):
    print(a + b)

result= add( 34,45)


# ----------------------------------------------------------
# Function without return.
#
# Python automatically returns None.
# ----------------------------------------------------------

def hello():
    print("Hi")

x = hello()

print(x)


# ----------------------------------------------------------
# Function with return.
#
# Now x stores "Hi".
# ----------------------------------------------------------

def hello():
    return "Hi"

x = hello()

print(x)


# ----------------------------------------------------------
# Returned value can be directly used
# inside another expression.
# ----------------------------------------------------------

def add(a, b):
    return a + b

print(add(10, 20) + 5)


# ----------------------------------------------------------
# Function Termination
#
# As soon as Python reaches return,
# the function immediately ends.
#
# print("B") never executes.
# ----------------------------------------------------------

def test():
    print("A")

    return

    print("B")

test()


# ----------------------------------------------------------
# Returning calculated values.
# ----------------------------------------------------------

def square(number):
    return number * number

result = square(5)

print(result)

# ----------------------------------------------------------
# Early Return
#
# Here the function returns immediately if age is less than 18.
# If return executes, the remaining lines are skipped.
# ----------------------------------------------------------

def check_age(age):
    if age < 18:
        return "Minor"

    print("Checking completed")

    return "Adult"

print(check_age(21))


# ----------------------------------------------------------
# Login Example
#
# This is similar to how authentication works.
# If the password is wrong, the function returns immediately.
# Otherwise the remaining code executes.
# ----------------------------------------------------------

def login(password):
    if password != "correct":
        return "Access Denied"

    print("Loading profile...")
    print("Loading messages...")
    print("Loading photos...")

    return "Welcome"


# ----------------------------------------------------------
# Another example showing that
# return immediately stops function execution.
# ----------------------------------------------------------

def test():
    print("A")
    return
    print("B")

print("Start")

test()

print("End")


# ----------------------------------------------------------
# Code after return never executes.
# Python exits the function before reaching print("Done").
# ----------------------------------------------------------

def add(a, b):
    return a + b
    print("Done")

print(add(2, 3))


# ----------------------------------------------------------
# Multiple Return Statements
#
# A function can have many return statements,
# but only one executes during a single function call.
# ----------------------------------------------------------

def check(number):
    if number > 0:
        return "Positive"

    return "Not Positive"

print(check(-5))


# ----------------------------------------------------------
# Function without return.
#
# Python automatically returns None.
# ----------------------------------------------------------

def hello():
    print("Hello")

x = hello()

print(x)


# ----------------------------------------------------------
# Real-world Function Chaining
#
# Imagine an online shopping app.
#
# get_cart()
# ↓
# calculate_total()
# ↓
# calculate_discount()
# ↓
# calculate_gst()
# ↓
# generate_invoice()
# ↓
# send_email()
#
# Each function returns data that becomes
# the input for the next function.
# ----------------------------------------------------------

# cart = get_cart()

# total = calculate_total(cart)

# discount = calculate_discount(total)

# gst = calculate_gst(discount)

# invoice = generate_invoice(gst)

# send_email(invoice)


# ----------------------------------------------------------
# Small Example Project
#
# One function returns marks.
# Another function calculates the grade.
# Another function prints the final result.
#
# This is an example of modular programming.
# ----------------------------------------------------------

def marks_of_student():
    return 75

def caluclate_grade(marks):

    if marks>90:
        return "A"

    if marks > 80:
        return "B"

    return "C"

def print_result():
    marks = marks_of_student()

    grade = caluclate_grade(marks)

    print("marks =",marks)
    print("grade =",grade)

print_result()


# ----------------------------------------------------------
# Local Scope
#
# There are two variables named "name".
#
# One is global.
# One is local.
#
# Python first checks the local scope.
# ----------------------------------------------------------

name = "Pavan"

def greet():
    name = "Rahul"
    print(name)

greet()

# Outside the function,
# the global variable still exists.

print(name)


# ----------------------------------------------------------
# Global Keyword
#
# Normally Python creates a local variable.
#
# Using global tells Python:
# "Use the global variable instead."
# ----------------------------------------------------------

count = 0

def increase():
    global count
    count = count + 1

increase()

print(count)


# ----------------------------------------------------------
# Another global keyword example.
#
# The global variable is modified
# from inside the function.
# ----------------------------------------------------------

name = "pavan"

def change():
    global name

    name = " bhanu"

change()

print(name)


# ----------------------------------------------------------
# Better Practice
#
# Instead of modifying a global variable,
# return the new value.
#
# This makes the function easier to understand
# and easier to test.
# ----------------------------------------------------------

def increase(count):
    return count + 1

count = 0

count = increase(count)

print(count)


# ----------------------------------------------------------
# nonlocal Keyword
#
# Used with nested functions.
#
# inner() changes the variable
# that belongs to outer().
# ----------------------------------------------------------

def outer():
    x=10

    def inner():
        nonlocal x
        x= 20

    inner()

    print(x)

outer()


# ==========================================================
# Lambda Function Practice
#
# Lambda is a small anonymous function.
# Mostly used for short operations.
# ==========================================================


# ----------------------------------------------------------
# Returning the larger number using a normal function.
# ----------------------------------------------------------

def larger( a, b ):
    if a>b:
        return a
    return b

larger(5,6)


# ----------------------------------------------------------
# Simple lambda function.
#
# Here we only created the lambda.
# It is not called.
# ----------------------------------------------------------

lambda a, b : a+b


# ----------------------------------------------------------
# Lambda function called immediately.
#
# (lambda ...)(arguments)
# ----------------------------------------------------------

(lambda a,b: a if a>b else b )( 8 , 62)


# ----------------------------------------------------------
# Storing a lambda function in a variable.
# ----------------------------------------------------------

large = lambda a,b : a if a>b else b

large(62 , 7)


# ----------------------------------------------------------
# Sorting tuples.
#
# Default sorting is based on
# the first element of each tuple.
# ----------------------------------------------------------

lst = [(12, 56) , (2, 4) , (5, 3)]

lst.sort()

lst


# ----------------------------------------------------------
# Custom Sorting
#
# Here key function returns
# the second element of each tuple.
#
# Python sorts based on that value.
# ----------------------------------------------------------

lst = [(12,56),(2,4),(5,3)]

def K(x):
    return x [1]

lst.sort(key = K)

lst


# ----------------------------------------------------------
# Same sorting using lambda.
#
# lambda replaces the separate K() function.
# ----------------------------------------------------------

lst.sort( key = lambda X : X[1])

lst


# ----------------------------------------------------------
# Printing even numbers from a list.
#
# The modulo operator (%) checks
# whether a number is divisible by 2.
# ----------------------------------------------------------

def even(li):
    for i in li:
        if i %2 == 0:
            print(i, end = " " )

lst = [1,2,4,6,9,7,10,46,68]

even(lst)


# ----------------------------------------------------------
# Finding unique elements.
#
# If an element is not already present
# in the new list, add it.
#
# This removes duplicate values.
# ----------------------------------------------------------

# unique

lst = [1,2,1,3,45,6,7,7]

def unique(li):
    new=[]

    for i in li:
        if i not in new :
            new.append(i)

    return new

unique(lst)


# ----------------------------------------------------------
# Multi-line greeting function.
#
# One function can execute
# multiple related statements.
# ----------------------------------------------------------

def greet(name):
    print(f"Welcome {name}")
    print("How are you?")
    print("Have a nice day!")

greet("pavan")

greet("kjnc")