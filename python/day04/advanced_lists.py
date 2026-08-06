"""
Mission 365
Python Lists - Day 02

Part 1A
Topic:
1. Basic Slicing
2. Start : Stop
3. Start : Stop : Step
"""

# ==========================================
# Basic Slicing
# ==========================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:])



numbers = [1, 2, 3, 4, 5]

print(numbers[:])



languages = ["Python", "Java", "Go", "C++"]

print(languages[:])



# ==========================================
# Start : Stop
# ==========================================

numbers = [10,20,30,40,50,60]

print(numbers[1:4])

print(numbers[2:5])

print(numbers[0:3])

print(numbers[3:6])



numbers = [5,10,15,20,25,30,35]

print(numbers[2:6])

print(numbers[1:5])

print(numbers[0:7])



# ==========================================
# Start Missing
# ==========================================

numbers = [10,20,30,40,50,60]

print(numbers[:2])

print(numbers[:3])

print(numbers[:4])

print(numbers[:5])



fruits = ["Apple","Banana","Mango","Orange","Kiwi"]

print(fruits[:2])

print(fruits[:4])



# ==========================================
# Stop Missing
# ==========================================

numbers = [10,20,30,40,50,60]

print(numbers[2:])

print(numbers[3:])

print(numbers[4:])

print(numbers[5:])



languages = ["Python","Java","Go","Rust","C"]

print(languages[1:])

print(languages[2:])



# ==========================================
# Whole List
# ==========================================

numbers = [100,200,300,400]

print(numbers[:])

print(numbers[::])



# ==========================================
# Step
# ==========================================

numbers = [10,20,30,40,50,60,70,80]

print(numbers[::2])

print(numbers[::3])

print(numbers[::4])



numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[1::2])

print(numbers[2::2])

print(numbers[3::2])



# ==========================================
# Start : Stop : Step
# ==========================================

numbers = [10,20,30,40,50,60,70,80,90]

print(numbers[1:8:2])

print(numbers[0:9:3])

print(numbers[2:8:2])

print(numbers[3:9:2])

print(numbers[1:7:3])



# ==========================================
# Different Slice Combinations
# ==========================================

numbers = [11,22,33,44,55,66,77,88]

print(numbers[0:4])

print(numbers[2:6])

print(numbers[1:7])

print(numbers[3:5])

print(numbers[4:8])



# ==========================================
# One Element Slice
# ==========================================

numbers = [10,20,30,40,50]

print(numbers[0:1])

print(numbers[2:3])

print(numbers[4:5])



# ==========================================
# Empty Slice
# ==========================================

numbers = [10,20,30,40]

print(numbers[2:2])

print(numbers[4:4])

print(numbers[3:1])



# ==========================================
# Store Slice in Variable
# ==========================================

numbers = [10,20,30,40,50,60]

first_half = numbers[:3]

second_half = numbers[3:]

middle = numbers[2:5]

print(first_half)

print(second_half)

print(middle)



# ==========================================
# Experiment Yourself
# ==========================================

numbers = [5,10,15,20,25,30,35,40]

print(numbers[1:6])

print(numbers[2:7])

print(numbers[:6])

print(numbers[3:])

print(numbers[::2])

print(numbers[::3])

print(numbers[1:7:2])

print(numbers[2:8:2])

print(numbers[:])

print(numbers[::])

# ==========================================
# More Start : Stop : Step Examples
# ==========================================

numbers = [10,20,30,40,50,60,70,80,90,100]

print(numbers[0:10:2])

print(numbers[1:10:2])

print(numbers[2:10:2])

print(numbers[0:9:3])

print(numbers[1:9:3])

print(numbers[2:9:3])

print(numbers[3:10:3])



# ==========================================
# Skip Different Number of Elements
# ==========================================

numbers = [5,10,15,20,25,30,35,40,45,50]

print(numbers[::2])

print(numbers[::3])

print(numbers[::4])

print(numbers[::5])



# ==========================================
# Slicing Strings Inside a List
# ==========================================

languages = [
    "Python",
    "Java",
    "C",
    "C++",
    "Go",
    "Rust",
    "JavaScript"
]

print(languages[:3])

print(languages[2:5])

print(languages[4:])

print(languages[::2])

print(languages[1::2])



# ==========================================
# Store Different Slices
# ==========================================

numbers = [10,20,30,40,50,60,70]

first = numbers[:2]

second = numbers[2:5]

third = numbers[5:]

print(first)

print(second)

print(third)



# ==========================================
# Copy Using Slicing
# ==========================================

numbers = [100,200,300,400]

copy_numbers = numbers[:]

print(numbers)

print(copy_numbers)



copy_numbers.append(500)

print(numbers)

print(copy_numbers)



# ==========================================
# Check Original List
# ==========================================

numbers = [1,2,3,4,5]

slice1 = numbers[:3]

slice2 = numbers[2:]

slice3 = numbers[1:4]

print(numbers)

print(slice1)

print(slice2)

print(slice3)



# ==========================================
# Slice with Variables
# ==========================================

numbers = [10,20,30,40,50,60,70,80]

start = 2

stop = 6

print(numbers[start:stop])



start = 1

stop = 7

step = 2

print(numbers[start:stop:step])



# ==========================================
# Real Practice
# ==========================================

marks = [95,80,76,88,91,65,72]

top_three = marks[:3]

last_three = marks[-3:]

middle_marks = marks[2:5]

print(top_three)

print(last_three)

print(middle_marks)



# ==========================================
# Student Names
# ==========================================

students = [
    "Ram",
    "Shyam",
    "Mohan",
    "Ravi",
    "Kiran",
    "Pavan",
    "Rahul"
]

print(students[:4])

print(students[3:])

print(students[1:6])

print(students[::2])



# ==========================================
# Predict the Output
# ==========================================

numbers = [11,22,33,44,55,66,77,88,99]

print(numbers[2:7])

print(numbers[0:5])

print(numbers[4:9])

print(numbers[1:8:2])

print(numbers[0:9:3])

print(numbers[:])

print(numbers[::])



# ==========================================
# More Practice
# ==========================================

numbers = [2,4,6,8,10,12,14,16]

print(numbers[:5])

print(numbers[2:])

print(numbers[1:6])

print(numbers[2:7:2])

print(numbers[::2])

print(numbers[::3])



# ==========================================
# Empty Slice Practice
# ==========================================

numbers = [10,20,30,40,50]

print(numbers[0:0])

print(numbers[1:1])

print(numbers[5:5])

print(numbers[4:2])



# ==========================================
# Mini Challenge
# ==========================================

numbers = [5,10,15,20,25,30,35,40]

first_four = numbers[:4]

last_four = numbers[4:]

alternate = numbers[::2]

middle = numbers[2:6]

copy_list = numbers[:]

print(first_four)

print(last_four)

print(alternate)

print(middle)

print(copy_list)



# ==========================================
# Experiment Yourself
# ==========================================

numbers = [100,200,300,400,500,600,700,800]

print(numbers[1:5])

print(numbers[2:6])

print(numbers[3:7])

print(numbers[::2])

print(numbers[1::2])

print(numbers[2::3])

print(numbers[:])

print(numbers[::])

print(numbers[4:])

print(numbers[:4])

# ==========================================
# Reverse Slicing
# ==========================================

numbers = [10,20,30,40,50]

print(numbers[::-1])



numbers = [10,20,30,40,50,60]

print(numbers[::-1])

print(numbers[::-2])

print(numbers[::-3])



# ==========================================
# Reverse from Particular Index
# ==========================================

numbers = [10,20,30,40,50,60]

print(numbers[4::-1])

print(numbers[3::-1])

print(numbers[2::-1])

print(numbers[5::-1])



# ==========================================
# Reverse with Start and Stop
# ==========================================

numbers = [10,20,30,40,50,60,70]

print(numbers[6:2:-1])

print(numbers[5:1:-1])

print(numbers[4:0:-1])

print(numbers[3:1:-1])



# ==========================================
# Reverse Different Lists
# ==========================================

numbers = [5,10,15,20,25,30]

print(numbers[::-1])

print(numbers[::-2])



fruits = ["Apple","Banana","Mango","Orange","Kiwi"]

print(fruits[::-1])



letters = ["A","B","C","D","E","F"]

print(letters[::-1])



# ==========================================
# Store Reverse in Variable
# ==========================================

numbers = [10,20,30,40,50]

reverse_numbers = numbers[::-1]

print(numbers)

print(reverse_numbers)



# ==========================================
# Reverse Copy
# ==========================================

numbers = [100,200,300,400]

copy_numbers = numbers[::-1]

copy_numbers.append(500)

print(numbers)

print(copy_numbers)



# ==========================================
# Negative Indexing
# ==========================================

numbers = [10,20,30,40,50]

print(numbers[-1])

print(numbers[-2])

print(numbers[-3])

print(numbers[-4])

print(numbers[-5])



# ==========================================
# More Negative Indexing
# ==========================================

numbers = [100,200,300,400,500,600]

print(numbers[-1])

print(numbers[-2])

print(numbers[-3])

print(numbers[-4])

print(numbers[-5])

print(numbers[-6])



# ==========================================
# Strings with Negative Index
# ==========================================

languages = [
    "Python",
    "Java",
    "Go",
    "Rust",
    "C++"
]

print(languages[-1])

print(languages[-2])

print(languages[-3])



# ==========================================
# Negative Slicing
# ==========================================

numbers = [10,20,30,40,50,60]

print(numbers[-4:-1])

print(numbers[-5:-2])

print(numbers[-3:])

print(numbers[:-2])

print(numbers[-6:-1])



# ==========================================
# More Negative Slicing
# ==========================================

numbers = [5,10,15,20,25,30,35]

print(numbers[-6:-2])

print(numbers[-5:-1])

print(numbers[-4:])

print(numbers[:-3])

print(numbers[-7:-3])



# ==========================================
# Last Elements
# ==========================================

numbers = [10,20,30,40,50,60]

last = numbers[-1]

second_last = numbers[-2]

third_last = numbers[-3]

print(last)

print(second_last)

print(third_last)



# ==========================================
# Experiment Yourself
# ==========================================

numbers = [11,22,33,44,55,66,77,88]

print(numbers[::-1])

print(numbers[::-2])

print(numbers[-1])

print(numbers[-2])

print(numbers[-5:-1])

print(numbers[-4:])

print(numbers[:-2])

print(numbers[6:1:-1])

print(numbers[5::-1])

print(numbers[::-3])


# ==========================================
# Mixing Positive and Negative Indexing
# ==========================================

numbers = [10,20,30,40,50,60,70,80]

print(numbers[1:-1])

print(numbers[2:-2])

print(numbers[3:-1])

print(numbers[1:-3])

print(numbers[2:-1])



# ==========================================
# More Mixed Slicing
# ==========================================

numbers = [5,10,15,20,25,30,35,40,45]

print(numbers[2:-2])

print(numbers[1:-1])

print(numbers[3:-3])

print(numbers[4:-1])

print(numbers[:-4])



# ==========================================
# Reverse + Negative Index
# ==========================================

numbers = [100,200,300,400,500]

print(numbers[::-1])

print(numbers[::-2])

print(numbers[-1])

print(numbers[-2])

print(numbers[-3])



# ==========================================
# Reverse Part of List
# ==========================================

numbers = [10,20,30,40,50,60,70]

print(numbers[6:2:-1])

print(numbers[5:0:-1])

print(numbers[4:1:-1])

print(numbers[3::-1])



# ==========================================
# Last N Elements
# ==========================================

numbers = [10,20,30,40,50,60,70]

print(numbers[-1:])

print(numbers[-2:])

print(numbers[-3:])

print(numbers[-4:])



# ==========================================
# Remove Last Elements Using Slicing
# ==========================================

numbers = [10,20,30,40,50,60]

print(numbers[:-1])

print(numbers[:-2])

print(numbers[:-3])

print(numbers[:-4])



# ==========================================
# Store Different Parts
# ==========================================

numbers = [100,200,300,400,500,600]

last = numbers[-1]

second_last = numbers[-2]

last_two = numbers[-2:]

last_three = numbers[-3:]

print(last)

print(second_last)

print(last_two)

print(last_three)



# ==========================================
# Reverse Copy Practice
# ==========================================

numbers = [11,22,33,44,55]

copy_list = numbers[::-1]

print(numbers)

print(copy_list)

copy_list.append(66)

print(numbers)

print(copy_list)



# ==========================================
# Check Original List
# ==========================================

numbers = [10,20,30,40]

reverse_list = numbers[::-1]

print(numbers)

print(reverse_list)

numbers.append(50)

print(numbers)

print(reverse_list)



# ==========================================
# Reverse Strings List
# ==========================================

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Kiwi"
]

print(fruits[::-1])

print(fruits[-1])

print(fruits[-2])

print(fruits[-3:])



# ==========================================
# Practice with Student Names
# ==========================================

students = [
    "Ram",
    "Rahul",
    "Pavan",
    "Sai",
    "Kiran",
    "Mohan"
]

print(students[-1])

print(students[-2])

print(students[-4:-1])

print(students[::-1])



# ==========================================
# Prediction Practice
# ==========================================

numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[-1])

print(numbers[-5])

print(numbers[-4:-1])

print(numbers[::-1])

print(numbers[::-2])

print(numbers[7:2:-1])

print(numbers[5::-1])



# ==========================================
# Small Challenge
# ==========================================

numbers = [10,20,30,40,50,60,70,80]

first_part = numbers[:4]

second_part = numbers[4:]

reverse = numbers[::-1]

alternate = numbers[::-2]

middle = numbers[2:-2]

print(first_part)

print(second_part)

print(reverse)

print(alternate)

print(middle)



# ==========================================
# Experiment Yourself
# ==========================================

numbers = [15,30,45,60,75,90,105,120]

print(numbers[-1])

print(numbers[-2])

print(numbers[-5:-1])

print(numbers[::-1])

print(numbers[::-3])

print(numbers[6:1:-1])

print(numbers[:-2])

print(numbers[-3:])

print(numbers[2:-2])

print(numbers[1:-1])

# ==========================================
# Copy using =
# ==========================================

a = [10,20,30]

b = a

print(a)

print(b)



# Change b

b[0] = 100

print(a)

print(b)



# ==========================================
# Another Example
# ==========================================

numbers = [1,2,3]

copy_numbers = numbers

copy_numbers.append(4)

print(numbers)

print(copy_numbers)



# ==========================================
# Strings List
# ==========================================

fruits = ["Apple","Banana","Orange"]

new_fruits = fruits

new_fruits.append("Mango")

print(fruits)

print(new_fruits)



# ==========================================
# Remove Element
# ==========================================

numbers = [10,20,30,40]

copy_numbers = numbers

copy_numbers.remove(20)

print(numbers)

print(copy_numbers)



# ==========================================
# Insert Element
# ==========================================

numbers = [100,200,300]

copy_numbers = numbers

copy_numbers.insert(1,150)

print(numbers)

print(copy_numbers)



# ==========================================
# Change Last Element
# ==========================================

numbers = [5,10,15,20]

copy_numbers = numbers

copy_numbers[-1] = 99

print(numbers)

print(copy_numbers)



# ==========================================
# Nested List Reference
# ==========================================

matrix = [
    [1,2],
    [3,4]
]

matrix2 = matrix

matrix2[0][1] = 999

print(matrix)

print(matrix2)



# ==========================================
# Check Object ID
# ==========================================

numbers = [10,20,30]

copy_numbers = numbers

print(id(numbers))

print(id(copy_numbers))



# ==========================================
# Another id() Example
# ==========================================

names = ["Ram","Rahul","Pavan"]

names2 = names

print(id(names))

print(id(names2))



# ==========================================
# Both Variables Point to Same Object
# ==========================================

a = [1,2,3]

b = a

print(a is b)

print(id(a))

print(id(b))



# ==========================================
# Changing Through First Variable
# ==========================================

a = [10,20,30]

b = a

a.append(40)

print(a)

print(b)



# ==========================================
# Changing Through Second Variable
# ==========================================

a = [10,20,30]

b = a

b.append(50)

print(a)

print(b)



# ==========================================
# Mixed Operations
# ==========================================

numbers = [1,2,3,4]

new_numbers = numbers

new_numbers.pop()

new_numbers.append(100)

new_numbers.insert(0,999)

print(numbers)

print(new_numbers)



# ==========================================
# Experiment Yourself
# ==========================================

numbers = [11,22,33,44]

copy_numbers = numbers

print(id(numbers))

print(id(copy_numbers))

copy_numbers[1] = 500

copy_numbers.append(600)

copy_numbers.remove(33)

print(numbers)

print(copy_numbers)



# ==========================================
# Practice
# ==========================================

marks = [85,90,95]

new_marks = marks

new_marks[0] = 100

new_marks.append(80)

print(marks)

print(new_marks)



# ==========================================
# Small Challenge
# ==========================================

students = ["Ram","Rahul","Pavan"]

students_copy = students

students_copy.append("Sai")

students_copy[0] = "Krishna"

print(students)

print(students_copy)

# ==========================================
# Copy using copy()
# ==========================================

numbers = [10,20,30]

copy_numbers = numbers.copy()

print(numbers)

print(copy_numbers)



copy_numbers.append(40)

print(numbers)

print(copy_numbers)



# ==========================================
# Modify First Element
# ==========================================

numbers = [100,200,300]

copy_numbers = numbers.copy()

copy_numbers[0] = 999

print(numbers)

print(copy_numbers)



# ==========================================
# Remove Element
# ==========================================

numbers = [5,10,15,20]

copy_numbers = numbers.copy()

copy_numbers.remove(10)

print(numbers)

print(copy_numbers)



# ==========================================
# Insert Element
# ==========================================

numbers = [10,20,30]

copy_numbers = numbers.copy()

copy_numbers.insert(1,15)

print(numbers)

print(copy_numbers)



# ==========================================
# Check id()
# ==========================================

numbers = [1,2,3]

copy_numbers = numbers.copy()

print(id(numbers))

print(id(copy_numbers))



# ==========================================
# Check is Operator
# ==========================================

numbers = [10,20,30]

copy_numbers = numbers.copy()

print(numbers is copy_numbers)



# ==========================================
# Copy using list()
# ==========================================

numbers = [10,20,30]

copy_numbers = list(numbers)

print(numbers)

print(copy_numbers)



copy_numbers.append(40)

print(numbers)

print(copy_numbers)



# ==========================================
# Another list() Example
# ==========================================

marks = [85,90,95]

new_marks = list(marks)

new_marks[1] = 100

print(marks)

print(new_marks)



# ==========================================
# list() with Strings
# ==========================================

fruits = ["Apple","Banana","Orange"]

new_fruits = list(fruits)

new_fruits.append("Mango")

print(fruits)

print(new_fruits)



# ==========================================
# Check id()
# ==========================================

numbers = [100,200,300]

copy_numbers = list(numbers)

print(id(numbers))

print(id(copy_numbers))

print(numbers is copy_numbers)



# ==========================================
# Copy using Slicing [:]
# ==========================================

numbers = [10,20,30]

copy_numbers = numbers[:]

print(numbers)

print(copy_numbers)



copy_numbers.append(40)

print(numbers)

print(copy_numbers)



# ==========================================
# Modify Element
# ==========================================

numbers = [5,10,15]

copy_numbers = numbers[:]

copy_numbers[2] = 100

print(numbers)

print(copy_numbers)



# ==========================================
# Remove Element
# ==========================================

numbers = [11,22,33,44]

copy_numbers = numbers[:]

copy_numbers.pop()

print(numbers)

print(copy_numbers)



# ==========================================
# Check id()
# ==========================================

numbers = [1,2,3]

copy_numbers = numbers[:]

print(id(numbers))

print(id(copy_numbers))

print(numbers is copy_numbers)



# ==========================================
# Compare All Three Methods
# ==========================================

numbers = [10,20,30]

copy1 = numbers.copy()

copy2 = list(numbers)

copy3 = numbers[:]

print(copy1)

print(copy2)

print(copy3)



copy1.append(40)

copy2.append(50)

copy3.append(60)

print(numbers)

print(copy1)

print(copy2)

print(copy3)



# ==========================================
# Experiment Yourself
# ==========================================

numbers = [100,200,300,400]

a = numbers.copy()

b = list(numbers)

c = numbers[:]

a[0] = 1

b[1] = 2

c[2] = 3

print(numbers)

print(a)

print(b)

print(c)

# ==========================================
# Shallow Copy
# ==========================================

a = [
    [1,2],
    [3,4]
]

b = a.copy()

print(a)

print(b)



# Change Inner List

b[0][0] = 999

print(a)

print(b)



# ==========================================
# Another Shallow Copy Example
# ==========================================

students = [
    ["Ram",85],
    ["Rahul",90]
]

students_copy = students.copy()

students_copy[1][1] = 100

print(students)

print(students_copy)



# ==========================================
# Append Inner List
# ==========================================

a = [
    [10,20],
    [30,40]
]

b = a.copy()

b[0].append(50)

print(a)

print(b)



# ==========================================
# Check id() of Outer List
# ==========================================

a = [
    [1,2],
    [3,4]
]

b = a.copy()

print(id(a))

print(id(b))



# ==========================================
# Check id() of Inner List
# ==========================================

print(id(a[0]))

print(id(b[0]))

print(a[0] is b[0])



# ==========================================
# Deep Copy
# ==========================================

import copy

a = [
    [1,2],
    [3,4]
]

b = copy.deepcopy(a)

print(a)

print(b)



# Change Inner List

b[0][0] = 999

print(a)

print(b)



# ==========================================
# Another Deep Copy Example
# ==========================================

matrix = [
    [10,20],
    [30,40]
]

new_matrix = copy.deepcopy(matrix)

new_matrix[1][1] = 500

print(matrix)

print(new_matrix)



# ==========================================
# Append to Inner List
# ==========================================

numbers = [
    [1,2],
    [3,4]
]

copy_numbers = copy.deepcopy(numbers)

copy_numbers[0].append(100)

print(numbers)

print(copy_numbers)



# ==========================================
# Check id() of Outer List
# ==========================================

a = [
    [5,6],
    [7,8]
]

b = copy.deepcopy(a)

print(id(a))

print(id(b))



# ==========================================
# Check id() of Inner List
# ==========================================

print(id(a[0]))

print(id(b[0]))

print(a[0] is b[0])



# ==========================================
# Compare Shallow vs Deep Copy
# ==========================================

original = [
    [100,200],
    [300,400]
]

shallow = original.copy()

deep = copy.deepcopy(original)

shallow[0][0] = 999

print(original)

print(shallow)

print(deep)



# ==========================================
# Compare Again
# ==========================================

original = [
    [10,20],
    [30,40]
]

shallow = original.copy()

deep = copy.deepcopy(original)

deep[1][1] = 777

print(original)

print(shallow)

print(deep)



# ==========================================
# Mixed Practice
# ==========================================

data = [
    ["Python",95],
    ["Java",90],
    ["Go",85]
]

data_copy = copy.deepcopy(data)

data_copy[2][1] = 100

print(data)

print(data_copy)



# ==========================================
# Practice with Nested Fruits List
# ==========================================

fruits = [
    ["Apple","Red"],
    ["Banana","Yellow"]
]

fruits_copy = fruits.copy()

fruits_copy[0][1] = "Green"

print(fruits)

print(fruits_copy)



# ==========================================
# Deep Copy with Fruits
# ==========================================

fruits = [
    ["Apple","Red"],
    ["Banana","Yellow"]
]

fruits_copy = copy.deepcopy(fruits)

fruits_copy[0][1] = "Green"

print(fruits)

print(fruits_copy)



# ==========================================
# Experiment Yourself
# ==========================================

marks = [
    [80,85],
    [90,95]
]

marks_copy = marks.copy()

marks_copy[1][0] = 100

print(marks)

print(marks_copy)



marks = [
    [80,85],
    [90,95]
]

marks_copy = copy.deepcopy(marks)

marks_copy[1][0] = 100

print(marks)

print(marks_copy)



# ==========================================
# Final Challenge
# ==========================================

original = [
    ["Ram",85],
    ["Rahul",90],
    ["Pavan",95]
]

copy1 = original.copy()

copy2 = copy.deepcopy(original)

copy1[0][1] = 100

copy2[2][1] = 99

print(original)

print(copy1)

print(copy2)