# Arrays - Day 02

## Second Largest Element in an Array

## Problem Statement

Given an array of integers, find the second largest distinct element in the array.

Example:

Input:
[8, 3, 15, 6, 11]

Output:
11

---

## Intuition

The idea is to keep track of the largest and second largest elements while traversing the array. Before jumping to the optimal solution, it's important to understand simpler approaches and then improve them step by step.

---

## Brute Force Approach

- Sort the array.
- Traverse from the end.
- Skip duplicate values.
- The first different element is the second largest.

---

## Better Approach

- Find the largest element in the first traversal.
- Traverse the array again.
- Ignore the largest element.
- Find the largest among the remaining elements.

---

## Optimal Approach

- Maintain two variables:
  - Largest
  - Second Largest
- Traverse the array only once.
- Update both variables whenever required.

---

## Dry Run

Array:

[12, 8, 25, 18, 30, 22]

Result:

Largest = 30

Second Largest = 25

---

## Time Complexity

| Approach | Time |
|----------|------|
| Brute Force | O(n log n) |
| Better | O(n) |
| Optimal | O(n) |

---

## Space Complexity

All three approaches use **O(1)** extra space.

---

## Real World Applications

- Finding the second highest score in a class.
- Ranking players in a competition.
- Finding the second highest salary.
- Analytics and leaderboard systems.

---

## Key Takeaways

- Every problem can have multiple approaches.
- Don't memorize the optimal solution.
- First understand the brute force solution, then improve it step by step.
- Dry runs make writing code much easier.

---

## Next Topic

Check if an Array is Sorted.