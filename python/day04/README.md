# 🚀 Engineer OS – Python

# 📚 Python Lists – Day 04

## 🎯 Module Goal

In this module, I learned advanced operations on Python Lists.

These concepts are used in:

- Backend Development
- AI & Machine Learning
- Data Science
- Automation
- Competitive Programming
- Software Development

This module focuses on understanding how Lists work internally, how Python stores them in memory, and how to manipulate them efficiently.

---

# 📖 1. Slicing

## What is Slicing?

Slicing is the process of extracting a portion (sub-list) from an existing list.

Instead of accessing one element at a time, slicing allows us to access multiple elements in a single statement.

It always returns a **new list**.

---

## Why do we use Slicing?

Slicing helps us to:

- Access multiple elements easily.
- Copy lists.
- Reverse lists.
- Skip elements.
- Split data into smaller parts.
- Process datasets efficiently.

---

## Syntax

```python
list[start : stop : step]
```

Where:

- **start** → Starting index (included)
- **stop** → Ending index (excluded)
- **step** → Number of positions to move

---

## Basic Slicing

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output

```python
[20,30,40]
```

Python starts from index 1 and stops before index 4.

---

## Start : Stop

```python
numbers = [10,20,30,40,50,60]

print(numbers[2:5])
```

Output

```python
[30,40,50]
```

---

## Missing Start

If the start index is omitted, Python starts from the beginning.

```python
numbers[:4]
```

Output

```python
[10,20,30,40]
```

---

## Missing Stop

If the stop index is omitted, Python goes until the end.

```python
numbers[3:]
```

Output

```python
[40,50,60]
```

---

## Complete Copy

```python
numbers[:]
```

Returns a new list containing all elements.

---

## Step Slicing

Step tells Python how many positions to move after selecting one element.

```python
numbers[::2]
```

Output

```python
[10,30,50]
```

Python skips every alternate element.

---

Another Example

```python
numbers[::3]
```

Output

```python
[10,40]
```

---

## Start : Stop : Step

```python
numbers[1:6:2]
```

Output

```python
[20,40,60]
```

Python:

- Starts at index 1
- Stops before index 6
- Moves 2 positions every time

---

## Reverse Slicing

Python can reverse a list using slicing.

```python
numbers[::-1]
```

Output

```python
[60,50,40,30,20,10]
```

The step becomes **-1**, so Python moves backwards.

---

## Copy using Slicing

```python
copy_numbers = numbers[:]
```

A completely new outer list is created.

The original list remains unchanged.

---

## Common Mistakes

### Mistake 1

Thinking the stop index is included.

```python
numbers[1:4]
```

Output

```python
[20,30,40]
```

Not

```python
[20,30,40,50]
```

The stop index is always excluded.

---

### Mistake 2

Using step = 0

```python
numbers[::0]
```

This raises an error because Python cannot move zero positions.

---

### Mistake 3

Thinking `numbers[::-1]` changes the original list.

It doesn't.

It creates a new reversed list.

---

## Best Practices

- Use slicing instead of loops for simple sub-lists.
- Use `[::-1]` when you need a reversed copy.
- Use `[:]` for creating a shallow copy of a list.
- Keep slicing expressions simple and readable.

---

# 📖 2. Negative Indexing

## What is Negative Indexing?

Negative indexing allows us to access elements from the end of a list.

Instead of counting from the beginning, Python starts counting from the last element.

---

## Why does Negative Indexing exist?

Suppose you want the last element.

Without negative indexing,

you would write

```python
numbers[len(numbers)-1]
```

Python provides a much simpler way.

```python
numbers[-1]
```

This is easier to read and write.

---

## Memory Representation

```
Positive Index

0    1    2    3    4

10   20   30   40   50

Negative Index

-5  -4  -3  -2  -1
```

Every element has two indexes.

---

## Access Last Element

```python
numbers[-1]
```

Output

```python
50
```

---

## Access Second Last Element

```python
numbers[-2]
```

Output

```python
40
```

---

## Access Third Last Element

```python
numbers[-3]
```

Output

```python
30
```

---

## Negative Slicing

```python
numbers[-4:-1]
```

Output

```python
[20,30,40]
```

Python starts from index -4 and stops before index -1.

---

Another Example

```python
numbers[-3:]
```

Output

```python
[30,40,50]
```

Returns the last three elements.

---

Another Example

```python
numbers[:-2]
```

Output

```python
[10,20,30]
```

Everything except the last two elements.

---

## Mixed Positive and Negative Indexing

```python
numbers[2:-1]
```

Output

```python
[30,40]
```

Python allows both positive and negative indexes in the same slicing operation.

---

## Real-World Usage

Negative indexing is useful in many situations.

Examples:

- Getting the latest chat message.
- Getting the last bank transaction.
- Reading the newest log entry.
- Accessing the latest GitHub commit.
- Getting the last record in a dataset.

---

## Common Mistakes

### Mistake 1

```python
numbers[-0]
```

Many beginners think this means the last element.

Actually,

```python
-0 == 0
```

So it returns the first element.

---

### Mistake 2

Using an invalid negative index.

```python
numbers[-10]
```

Raises

```python
IndexError
```

if the list is smaller.

---

### Mistake 3

Confusing indexing with slicing.

```python
numbers[-1]
```

Returns a single value.

```python
numbers[-1:]
```

Returns a list.

---

## Best Practices

- Use `-1` to access the last element.
- Use `-2` for the second last element.
- Use negative slicing when working with the end of large datasets.
- Prefer negative indexing instead of `len(list)-1` whenever possible.


# 📖 3. Copying Lists

## What is Copying?

Copying means creating another list from an existing list.

Python provides multiple ways to copy a list.

However, not all copying methods behave the same way.

Some methods create a completely new list.

Some methods only create another reference to the same list.

Understanding the difference is very important because it helps avoid unexpected bugs in real-world applications.

---

## Why do we Copy Lists?

Suppose you have a list of student marks.

```python
marks = [80, 90, 95]
```

You want to modify the marks without changing the original list.

Instead of changing the original list, you create a copy and work on it.

This is useful in:

- Data Analysis
- AI & Machine Learning
- Backend APIs
- Automation Scripts
- Games
- Image Processing

---

# Assignment (=)

## Definition

Using the assignment operator (`=`) does **not create a new list**.

Instead, it creates another variable pointing to the same list in memory.

---

## Syntax

```python
b = a
```

---

## Example

```python
a = [10,20,30]

b = a

b.append(40)

print(a)

print(b)
```

Output

```python
[10,20,30,40]

[10,20,30,40]
```

Both variables changed because both are pointing to the same list.

---

## Memory Representation

```
a
 \
  \
   ------> [10,20,30]
  /
 /
b
```

There is only **one list** in memory.

Both variables share it.

---

## Checking with id()

```python
a = [10,20,30]

b = a

print(id(a))

print(id(b))
```

Both IDs are the same because both variables point to the same object.

---

# copy()

## Definition

The `copy()` method creates a **new outer list**.

The original list remains unchanged.

---

## Syntax

```python
copy_list = original.copy()
```

---

## Example

```python
numbers = [10,20,30]

copy_numbers = numbers.copy()

copy_numbers.append(40)

print(numbers)

print(copy_numbers)
```

Output

```python
[10,20,30]

[10,20,30,40]
```

The original list is safe.

---

## Memory Representation

```
numbers

↓

[10,20,30]


copy_numbers

↓

[10,20,30]
```

Two different outer lists are created.

---

# list()

## Definition

The `list()` constructor also creates a new list.

It can also convert other iterable objects into lists.

---

## Syntax

```python
copy_list = list(original)
```

---

## Example

```python
numbers = [1,2,3]

copy_numbers = list(numbers)

copy_numbers.append(4)

print(numbers)

print(copy_numbers)
```

Output

```python
[1,2,3]

[1,2,3,4]
```

---

# Copy using Slicing

Another way to create a copy is by using slicing.

---

## Syntax

```python
copy_list = original[:]
```

---

## Example

```python
numbers = [100,200,300]

copy_numbers = numbers[:]

copy_numbers.append(400)

print(numbers)

print(copy_numbers)
```

Output

```python
[100,200,300]

[100,200,300,400]
```

The original list does not change.

---

# Comparison

| Method | Creates New List | Original Changes |
|----------|-----------------|------------------|
| `=` | ❌ No | ✅ Yes |
| `.copy()` | ✅ Yes | ❌ No |
| `list()` | ✅ Yes | ❌ No |
| `[:]` | ✅ Yes | ❌ No |

---

# What is a Reference?

A **reference** is simply the memory address of an object.

Variables do not store the actual list.

They store the address where the list exists in memory.

That is why

```python
b = a
```

does not create another list.

It only copies the reference.

---

# Shallow Copy

## Definition

A **Shallow Copy** creates a new outer list but keeps the inner (nested) objects shared.

This means changes made to nested lists will affect both copies.

---

## Example

```python
a = [
    [1,2],
    [3,4]
]

b = a.copy()

b[0][0] = 999

print(a)

print(b)
```

Output

```python
[[999,2],[3,4]]

[[999,2],[3,4]]
```

Both lists changed because the inner list is shared.

---

## Memory Representation

```
Outer List A
      │
      ▼
    [1,2]
      ▲
      │
Outer List B
```

Only the outer list is copied.

The nested lists remain the same objects.

---

# Deep Copy (Introduction)

## Definition

A **Deep Copy** creates a completely independent copy of every object, including nested lists.

Nothing is shared.

---

## Syntax

```python
import copy

new_list = copy.deepcopy(old_list)
```

---

## Example

```python
import copy

a = [
    [1,2],
    [3,4]
]

b = copy.deepcopy(a)

b[0][0] = 999

print(a)

print(b)
```

Output

```python
[[1,2],[3,4]]

[[999,2],[3,4]]
```

The original list remains unchanged.

---

## Memory Representation

```
Original

↓

Outer List

↓

Inner Lists


Deep Copy

↓

Another Outer List

↓

Another Set of Inner Lists
```

Everything is copied independently.

---

# Shallow Copy vs Deep Copy

| Shallow Copy | Deep Copy |
|---------------|-----------|
| Copies only the outer list | Copies every object |
| Nested lists are shared | Nested lists are independent |
| Faster | Slightly slower |
| Uses less memory | Uses more memory |

---

# Best Practices

- Use `=` only when you intentionally want two variables to share the same list.
- Use `.copy()` for normal one-dimensional lists.
- Use `list()` when converting iterables into lists.
- Use `[:]` for creating a quick shallow copy.
- Use `deepcopy()` whenever you work with nested lists and need completely independent data.

---

# Common Mistakes

### Mistake 1

Thinking

```python
b = a
```

creates another list.

It does not.

It only copies the reference.

---

### Mistake 2

Using `.copy()` with nested lists and expecting a completely independent copy.

`.copy()` performs only a shallow copy.

---

### Mistake 3

Forgetting to import the `copy` module before using `deepcopy()`.

```python
import copy
```

is required.

---

# Interview Questions

1. What is the difference between `=` and `.copy()`?
2. What is a reference?
3. What is a shallow copy?
4. What is a deep copy?
5. Why do nested lists change after using `.copy()`?
6. Which module provides `deepcopy()`?
7. When should you use `deepcopy()`?

# 📖 4. Sorting

## What is Sorting?

Sorting is the process of arranging data in a specific order.

Usually, data is sorted in:

- Ascending Order (Small → Large)
- Descending Order (Large → Small)

Sorting makes searching, analyzing, and displaying data much easier.

---

## Why do we use Sorting?

Sorting is used in many real-world applications.

Examples:

- Student marks ranking
- Product prices
- Employee salaries
- Bank transactions
- Online shopping websites
- Search results
- Leaderboards

---

# sort()

## Definition

The `sort()` method sorts the original list.

It changes the existing list permanently.

---

## Syntax

```python
list.sort()
```

---

## Example

```python
numbers = [40,10,30,20]

numbers.sort()

print(numbers)
```

Output

```python
[10,20,30,40]
```

---

## Descending Order

```python
numbers.sort(reverse=True)
```

Output

```python
[40,30,20,10]
```

---

## Important

`sort()` returns **None** because it modifies the original list directly.

---

# sorted()

## Definition

`sorted()` creates a new sorted list.

The original list remains unchanged.

---

## Syntax

```python
sorted(list)
```

---

## Example

```python
numbers = [40,10,30,20]

new_numbers = sorted(numbers)

print(numbers)

print(new_numbers)
```

Output

```python
[40,10,30,20]

[10,20,30,40]
```

---

# key Parameter

## What is key?

The `key` parameter tells Python what value should be used while sorting.

Instead of comparing the original elements, Python compares the value returned by the key function.

---

## Example

```python
words = [
    "Python",
    "C",
    "Java",
    "JavaScript"
]

words.sort(key=len)

print(words)
```

Output

```python
['C','Java','Python','JavaScript']
```

Python sorts according to the length of each word.

---

# lambda

## What is lambda?

A lambda function is a small anonymous function.

It is mostly used for short operations.

One of its biggest uses is sorting.

---

## Example

```python
students = [
    ("Ram",85),
    ("Rahul",95),
    ("Pavan",90)
]

students.sort(key=lambda x:x[1])

print(students)
```

Output

```python
[
('Ram',85),
('Pavan',90),
('Rahul',95)
]
```

Python sorts using the second value of every tuple.

---

## Descending Order

```python
students.sort(
    key=lambda x:x[1],
    reverse=True
)
```

Output

```python
[
('Rahul',95),
('Pavan',90),
('Ram',85)
]
```

---

# sort() vs sorted()

| sort() | sorted() |
|----------|-----------|
| Changes original list | Creates a new list |
| Returns None | Returns a new sorted list |
| Works only with lists | Works with any iterable |
| Uses less memory | Uses more memory |

---

# Best Practices

- Use `sort()` when you want to permanently change the list.
- Use `sorted()` when the original data must remain unchanged.
- Use `key` for custom sorting.
- Use `lambda` for short sorting operations.

---

# 📖 5. Reverse

## Why do we Reverse Lists?

Sometimes we need to process data from the end instead of the beginning.

Examples:

- Latest messages
- Recent transactions
- Newest notifications
- Latest commits
- Recent logs

---

# reverse()

## Definition

`reverse()` reverses the original list.

---

## Syntax

```python
list.reverse()
```

---

## Example

```python
numbers = [10,20,30,40]

numbers.reverse()

print(numbers)
```

Output

```python
[40,30,20,10]
```

---

# reversed()

## Definition

`reversed()` returns a reverse iterator.

The original list remains unchanged.

---

## Example

```python
numbers = [10,20,30]

print(list(reversed(numbers)))
```

Output

```python
[30,20,10]
```

---

# Reverse using Slicing

```python
numbers[::-1]
```

Example

```python
numbers = [10,20,30]

print(numbers[::-1])
```

Output

```python
[30,20,10]
```

---

# reverse() vs reversed() vs [::-1]

| Method | Original List | Returns |
|----------|--------------|----------|
| reverse() | Changes | None |
| reversed() | Unchanged | Iterator |
| [::-1] | Unchanged | New List |

---

# Best Practices

- Use `reverse()` when changing the original list.
- Use `reversed()` for iteration.
- Use `[::-1]` when a reversed copy is needed.

---

# 📖 6. Nested Lists

## What is a Nested List?

A Nested List is a list that contains one or more lists inside it.

It is also called a **2D List**.

---

## Example

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

---

## Real-World Examples

Nested Lists are used to represent:

- Tables
- Excel Sheets
- Chess Boards
- Game Maps
- Student Records
- Images (Pixels)
- AI Datasets

---

## Accessing Elements

```python
matrix[0]
```

Output

```python
[1,2,3]
```

---

```python
matrix[1][2]
```

Output

```python
6
```

---

## Updating Values

```python
matrix[1][1] = 100
```

Updated Matrix

```python
[
    [1,2,3],
    [4,100,6],
    [7,8,9]
]
```

---

## Traversing Nested Lists

### Using One Loop

```python
for row in matrix:
    print(row)
```

Output

```python
[1,2,3]

[4,5,6]

[7,8,9]
```

---

### Using Nested Loops

```python
for row in matrix:
    for value in row:
        print(value)
```

Output

```python
1
2
3
4
5
6
7
8
9
```

---

# Best Practices

- Use Nested Lists for table-like data.
- Use meaningful variable names like `matrix`, `rows`, and `columns`.
- Avoid modifying nested lists accidentally after a shallow copy.
- Use `deepcopy()` when working with nested data.

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Update | O(1) |
| Search | O(n) |
| Append | O(1) Average |
| Insert | O(n) |
| Remove | O(n) |
| Sort | O(n log n) |
| Reverse | O(n) |
| Slicing | O(k) |

---

# Common Interview Questions

1. What is slicing?
2. Why is the stop index excluded in slicing?
3. What is negative indexing?
4. Difference between indexing and slicing?
5. Difference between `=` and `.copy()`?
6. What is a reference?
7. What is a shallow copy?
8. What is a deep copy?
9. Why do nested lists change after `.copy()`?
10. Which module provides `deepcopy()`?
11. Difference between `sort()` and `sorted()`?
12. Why does `sort()` return `None`?
13. What is the purpose of `key`?
14. Why do we use `lambda` in sorting?
15. Difference between `reverse()` and `reversed()`?
16. Difference between `reverse()` and `[::-1]`?
17. What is a Nested List?
18. How do you access elements in a Nested List?
19. How do you traverse a Nested List?
20. When should you use `deepcopy()`?

---

# 🎯 Module Summary

After completing this module, I can confidently:

- ✅ Understand how slicing works.
- ✅ Use `start : stop : step`.
- ✅ Reverse lists using slicing.
- ✅ Use negative indexing.
- ✅ Copy lists correctly.
- ✅ Understand references in Python.
- ✅ Differentiate between shallow copy and deep copy.
- ✅ Sort data using `sort()` and `sorted()`.
- ✅ Sort using `key` and `lambda`.
- ✅ Reverse lists using different methods.
- ✅ Work with Nested Lists.
- ✅ Access, update, and traverse Nested Lists.

---

# 🚀 Mission 365 – Python Day 04 Completed

## Topics Covered

- ✅ Slicing
- ✅ Negative Indexing
- ✅ Copying Lists
- ✅ Reference
- ✅ Shallow Copy
- ✅ Deep Copy (Introduction)
- ✅ Sorting
- ✅ sort()
- ✅ sorted()
- ✅ key
- ✅ lambda
- ✅ reverse()
- ✅ reversed()
- ✅ Nested Lists

These concepts form an important foundation for Data Structures & Algorithms (DSA), Backend Development, AI/ML, Automation, and Technical Interviews.