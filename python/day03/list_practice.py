# ==========================================
# Python Lists Practice - 
# Basics + Creating + Access + Update
# ==========================================

# Creating Lists

numbers = [10, 20, 30, 40, 50]
print(numbers)

names = ["Ram", "Shyam", "Mohan"]
print(names)

mixed = [10, "Python", 9.5, True]
print(mixed)

empty = []
print(empty)

# ------------------------------------------

# Accessing Elements

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])

# ------------------------------------------

# Updating Elements

numbers[1] = 100
print(numbers)

names[0] = "Ravi"
print(names)

# ------------------------------------------

# Length

print(len(numbers))
print(len(names))

# ------------------------------------------

# Membership

print(100 in numbers)
print(500 in numbers)

print("Ravi" in names)
print("Ram" in names)

# ------------------------------------------

# Append

numbers.append(60)
print(numbers)

names.append("Kiran")
print(names)

# ------------------------------------------

# Extend

numbers.extend([70, 80, 90])
print(numbers)

names.extend(["Hari", "Teja"])
print(names)

# ------------------------------------------

# Insert

numbers.insert(0, 5)
print(numbers)

numbers.insert(3, 999)
print(numbers)

# ------------------------------------------

# Remove

numbers.remove(999)
print(numbers)

names.remove("Hari")
print(names)

# ------------------------------------------

# Pop

numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)

# ------------------------------------------

# Clear

temp = [1,2,3]

temp.clear()

print(temp)

# ------------------------------------------

# Del

a = [10,20,30,40]

del a[1]

print(a)

# ------------------------------------------

# Traversing

for num in numbers:
    print(num)

# ------------------------------------------

# Traversing using Index

for i in range(len(numbers)):
    print(i, numbers[i])

# ------------------------------------------

# While Loop

i = 0

while i < len(names):
    print(names[i])
    i += 1

# ------------------------------------------

# Enumerate

for index, value in enumerate(numbers):
    print(index, value)

# ------------------------------------------

# Search

print(30 in numbers)
print(300 in numbers)

print(numbers.count(30))

if 30 in numbers:
    print(numbers.index(30))

# ------------------------------------------

# ==========================================
# Python Lists Practice - 
# Sorting + Slicing + Copy + Nested Lists
# ==========================================


# -----------------------------
# Sorting
# -----------------------------

numbers = [50, 10, 40, 20, 30]

print(numbers)

numbers.sort()

print(numbers)


# Descending Order

numbers.sort(reverse=True)

print(numbers)


# -----------------------------
# sorted()
# -----------------------------

marks = [90, 60, 100, 75, 80]

new_marks = sorted(marks)

print(marks)
print(new_marks)


# -----------------------------
# reverse()
# -----------------------------

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


# -----------------------------
# Sorting Strings
# -----------------------------

fruits = ["Mango", "Apple", "Banana", "Orange"]

fruits.sort()

print(fruits)

fruits.sort(reverse=True)

print(fruits)


# -----------------------------
# key = len
# -----------------------------

words = ["Python", "C", "Java", "JavaScript", "Go"]

words.sort(key=len)

print(words)


# -----------------------------
# lambda
# -----------------------------

students = [
    ("Ram", 85),
    ("Shyam", 95),
    ("Mohan", 75),
    ("Ravi", 88)
]

students.sort(key=lambda x: x[1])

print(students)

students.sort(key=lambda x: x[1], reverse=True)

print(students)


# -----------------------------
# Basic Slicing
# -----------------------------

numbers = [10,20,30,40,50,60,70,80]

print(numbers[2:6])

print(numbers[:4])

print(numbers[3:])

print(numbers[:])

print(numbers[::2])

print(numbers[1::2])

print(numbers[::-1])

print(numbers[::-2])


# -----------------------------
# Negative Index
# -----------------------------

print(numbers[-1])

print(numbers[-3:])

print(numbers[-5:-2])


# -----------------------------
# Slice Assignment
# -----------------------------

numbers = [10,20,30,40,50]

numbers[1:3] = [200,300]

print(numbers)


numbers[1:3] = []

print(numbers)


numbers[1:1] = [20,30]

print(numbers)


# -----------------------------
# Copy using =
# -----------------------------

a = [10,20,30]

b = a

b[0] = 100

print(a)

print(b)


# -----------------------------
# copy()
# -----------------------------

a = [10,20,30]

b = a.copy()

b[0] = 500

print(a)

print(b)


# -----------------------------
# list()
# -----------------------------

a = [1,2,3]

b = list(a)

b.append(4)

print(a)

print(b)


# -----------------------------
# Slicing Copy
# -----------------------------

a = [100,200,300]

b = a[:]

b.append(400)

print(a)

print(b)


# -----------------------------
# Shallow Copy
# -----------------------------

a = [
    [1,2],
    [3,4]
]

b = a.copy()

b[0][0] = 999

print(a)

print(b)


# -----------------------------
# Deep Copy
# -----------------------------

import copy

a = [
    [1,2],
    [3,4]
]

b = copy.deepcopy(a)

b[0][0] = 999

print(a)

print(b)


# -----------------------------
# Nested Lists
# -----------------------------

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

print(matrix[0])

print(matrix[1])

print(matrix[2])


print(matrix[0][0])

print(matrix[1][2])

print(matrix[2][1])


# -----------------------------
# Update Nested List
# -----------------------------

matrix[1][1] = 100

print(matrix)


# -----------------------------
# Print Every Row
# -----------------------------

for row in matrix:
    print(row)


# -----------------------------
# Print Every Element
# -----------------------------

for row in matrix:
    for value in row:
        print(value)


# -----------------------------
# Using Index
# -----------------------------

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])


# -----------------------------
# Add New Row
# -----------------------------

matrix.append([10,11,12])

print(matrix)


# -----------------------------
# Add New Column
# -----------------------------

for row in matrix:
    row.append(0)

print(matrix)


# -----------------------------
# Remove Row
# -----------------------------

matrix.pop(1)

print(matrix)


# -----------------------------
# Remove One Element
# -----------------------------

matrix[0].pop(2)

print(matrix)


# -----------------------------
# Student Data
# -----------------------------

students = [
    ["Ram",90],
    ["Shyam",85],
    ["Mohan",95],
    ["Ravi",88]
]

for student in students:
    print(student)


for student in students:
    print(student[0])


for student in students:
    print(student[1])


for student in students:
    print(student[0], student[1])


# -----------------------------
# Find Total Marks
# -----------------------------

total = 0

for student in students:
    total += student[1]

print(total)


average = total / len(students)

print(average)


# -----------------------------
# Highest Marks
# -----------------------------

highest = students[0]

for student in students:

    if student[1] > highest[1]:
        highest = student

print(highest)


# -----------------------------
# Lowest Marks
# -----------------------------

lowest = students[0]

for student in students:

    if student[1] < lowest[1]:
        lowest = student

print(lowest)


# -----------------------------
# Search Student
# -----------------------------

name = "Mohan"

for student in students:

    if student[0] == name:
        print(student)


# ==========================================
# Python Lists Practice -
# List Comprehension + Built-in Functions
# Placement Practice
# ==========================================


# ------------------------------------------
# List Comprehension
# ------------------------------------------

numbers = [x for x in range(1, 11)]

print(numbers)


# ------------------------------------------
# Square Numbers
# ------------------------------------------

squares = [x * x for x in range(1, 11)]

print(squares)


# ------------------------------------------
# Cube Numbers
# ------------------------------------------

cubes = [x ** 3 for x in range(1, 11)]

print(cubes)


# ------------------------------------------
# Even Numbers
# ------------------------------------------

evens = [x for x in range(1, 21) if x % 2 == 0]

print(evens)


# ------------------------------------------
# Odd Numbers
# ------------------------------------------

odds = [x for x in range(1, 21) if x % 2 != 0]

print(odds)


# ------------------------------------------
# Upper Case
# ------------------------------------------

names = ["ram", "shyam", "mohan", "ravi"]

upper_names = [name.upper() for name in names]

print(upper_names)


# ------------------------------------------
# Lower Case
# ------------------------------------------

names = ["RAM", "SHYAM", "MOHAN"]

lower_names = [name.lower() for name in names]

print(lower_names)


# ------------------------------------------
# Length of Every Word
# ------------------------------------------

languages = ["Python", "Java", "Go", "JavaScript"]

lengths = [len(language) for language in languages]

print(lengths)


# ------------------------------------------
# Even / Odd
# ------------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,10]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)


# ------------------------------------------
# Filter Greater Than 50
# ------------------------------------------

marks = [35,60,75,42,91,88,49]

passed = [mark for mark in marks if mark >= 50]

print(passed)


# ------------------------------------------
# Flatten Nested List
# ------------------------------------------

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = [value for row in matrix for value in row]

print(flat)


# ==========================================
# Built-in Functions
# ==========================================

numbers = [10,20,30,40,50]

print(len(numbers))

print(min(numbers))

print(max(numbers))

print(sum(numbers))

print(sum(numbers) / len(numbers))


# ------------------------------------------
# any()
# ------------------------------------------

values = [0,0,5,0]

print(any(values))

values = [0,False,None]

print(any(values))


# ------------------------------------------
# all()
# ------------------------------------------

values = [1,2,3]

print(all(values))

values = [1,2,0]

print(all(values))


# ------------------------------------------
# sorted()
# ------------------------------------------

numbers = [40,10,30,20]

print(sorted(numbers))

print(sorted(numbers, reverse=True))

print(numbers)


# ------------------------------------------
# reversed()
# ------------------------------------------

numbers = [1,2,3,4,5]

print(list(reversed(numbers)))

print(numbers)


# ------------------------------------------
# zip()
# ------------------------------------------

names = ["Ram","Shyam","Mohan"]

marks = [90,80,95]

students = list(zip(names, marks))

print(students)


for name, mark in zip(names, marks):
    print(name, mark)


# ==========================================
# Placement Practice
# ==========================================

numbers = [45,12,67,89,34,23,90,11]

largest = max(numbers)

print(largest)


smallest = min(numbers)

print(smallest)


total = sum(numbers)

print(total)


average = sum(numbers) / len(numbers)

print(average)


# ------------------------------------------
# Count Even Numbers
# ------------------------------------------

count = 0

for num in numbers:

    if num % 2 == 0:
        count += 1

print(count)


# ------------------------------------------
# Count Odd Numbers
# ------------------------------------------

count = 0

for num in numbers:

    if num % 2 != 0:
        count += 1

print(count)


# ------------------------------------------
# Find Duplicates
# ------------------------------------------

numbers = [10,20,10,30,20,40,50]

duplicates = []

for num in numbers:

    if numbers.count(num) > 1:

        if num not in duplicates:

            duplicates.append(num)

print(duplicates)


# ------------------------------------------
# Remove Duplicates
# ------------------------------------------

numbers = [10,20,10,30,20,40]

unique = []

for num in numbers:

    if num not in unique:

        unique.append(num)

print(unique)


# ------------------------------------------
# Second Largest
# ------------------------------------------

numbers = [12,45,78,34,90,67]

numbers.sort()

print(numbers[-2])


# ------------------------------------------
# Reverse Without reverse()
# ------------------------------------------

numbers = [10,20,30,40,50]

print(numbers[::-1])


# ------------------------------------------
# Merge Lists
# ------------------------------------------

list1 = [1,2,3]

list2 = [4,5,6]

merged = list1 + list2

print(merged)


# ------------------------------------------
# Common Elements
# ------------------------------------------

list1 = [1,2,3,4,5]

list2 = [4,5,6,7]

common = []

for num in list1:

    if num in list2:

        common.append(num)

print(common)


# ------------------------------------------
# Difference
# ------------------------------------------

difference = []

for num in list1:

    if num not in list2:

        difference.append(num)

print(difference)


# ------------------------------------------
# Palindrome Check
# ------------------------------------------

numbers = [1,2,3,2,1]

if numbers == numbers[::-1]:

    print("Palindrome")

else:

    print("Not Palindrome")


# ------------------------------------------
# Rotate Left
# ------------------------------------------

numbers = [1,2,3,4,5]

rotated = numbers[1:] + numbers[:1]

print(rotated)


# ------------------------------------------
# Rotate Right
# ------------------------------------------

numbers = [1,2,3,4,5]

rotated = numbers[-1:] + numbers[:-1]

print(rotated)


# ------------------------------------------
# Frequency of Elements
# ------------------------------------------

numbers = [10,20,20,30,30,30]

for num in sorted(set(numbers)):

    print(num, ":", numbers.count(num))


# ------------------------------------------
# Student Records
# ------------------------------------------

students = [
    ["Ram",90],
    ["Shyam",85],
    ["Mohan",95],
    ["Ravi",70]
]

students.sort(key=lambda x: x[1], reverse=True)

print(students)


# ------------------------------------------
# Topper
# ------------------------------------------

print(students[0])


# ------------------------------------------
# Lowest Marks
# ------------------------------------------

print(students[-1])


# ------------------------------------------
# Pass Students
# ------------------------------------------

for student in students:

    if student[1] >= 80:

        print(student)


# ------------------------------------------
# Fail Students
# ------------------------------------------

for student in students:

    if student[1] < 80:

        print(student)


# ------------------------------------------
# Search Student
# ------------------------------------------

search = "Ram"

found = False

for student in students:

    if student[0] == search:

        print(student)

        found = True

        break

if not found:

    print("Student Not Found")


# ------------------------------------------
# List of Names Only
# ------------------------------------------

names = [student[0] for student in students]

print(names)


# ------------------------------------------
# List of Marks Only
# ------------------------------------------

marks = [student[1] for student in students]

print(marks)

