# 🚀 Move Zeroes (LeetCode 283)

## 📌 Problem

Given an integer array, move all `0`s to the end while keeping the relative order of the non-zero elements the same.

The array should be modified **in-place**, without creating another array.

---

## 💡 Approach

This problem can be solved efficiently using the **Two Pointers** technique.

- A **Read Pointer** traverses the entire array.
- A **Write Pointer** keeps track of where the next non-zero element should be placed.
- Whenever a non-zero element is found:
  - Copy it to the Write Pointer position.
  - Move the Write Pointer forward.
- After all non-zero elements are placed, fill the remaining positions with `0`.

---

## 🧠 Example

### Input

```text
[4,0,5,0,0,8]
```

### After Moving Non-Zero Elements

```text
[4,5,8,0,0,8]
```

### Final Output

```text
[4,5,8,0,0,0]
```

---

## 📝 Algorithm

1. Initialize the Write Pointer at index `0`.
2. Traverse the array using the Read Pointer.
3. If the current element is not `0`:
   - Copy it to the Write Pointer position.
   - Move the Write Pointer forward.
4. After traversal, fill the remaining positions with `0`.
5. The array is now updated in-place.

---

## ⏱ Time Complexity

**O(n)**

- One pass to move all non-zero elements.
- One pass to fill the remaining positions with zeroes.
- Overall complexity remains **O(n)**.

---

## 💾 Space Complexity

**O(1)**

- No extra array is used.
- The array is modified in-place.

---

## 📚 Concepts Learned

- Arrays
- Two Pointers
- In-place Array Modification
- Linear Traversal
- Time Complexity Analysis
- Space Complexity Analysis.

---

## 🎯 Interview Takeaway

Whenever a problem asks you to:

- Modify an array in-place
- Keep the order of elements
- Move specific elements (like zeroes)

Think about the **Two Pointers** pattern before considering more complex solutions.

---


# Left Rotate an Array by D Positions

## Problem Statement

Given an array and a number `D`, rotate the array to the left by `D` positions.

## Example

```text
Input:
[1, 2, 3, 4, 5, 6, 7]
D = 3

Output:
[4, 5, 6, 7, 1, 2, 3]
```

## Intuition

In a left rotation, the first `D` elements move to the end, while the remaining elements shift to the left by `D` positions.

For example:

```text
[1, 2, 3 | 4, 5, 6, 7]
              ↓
[4, 5, 6, 7 | 1, 2, 3]
```

## Brute Force Approach

Rotate the array one position at a time and repeat this `D` times.

**Time Complexity:** `O(n × D)`

**Space Complexity:** `O(1)`

## Better Approach

Save the first `D` elements in a temporary array, shift the remaining elements left by `D` positions, and place the saved elements at the end.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(D)`

## Optimal Approach

Use the **Reversal Algorithm**.

For left rotation by `D`:

1. Reverse the first `D` elements.
2. Reverse the remaining elements.
3. Reverse the entire array.

Example:

```text
[1, 2, 3 | 4, 5, 6, 7]

Reverse first part:
[3, 2, 1 | 4, 5, 6, 7]

Reverse second part:
[3, 2, 1 | 7, 6, 5, 4]

Reverse everything:
[4, 5, 6, 7 | 1, 2, 3]
```

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

## Why `D % n`?

If `D` is greater than the array length, some rotations are repeated.

For example:

```text
n = 5
D = 7

7 % 5 = 2
```

Rotating by 7 positions is the same as rotating by 2 positions.

## When to Use Each Approach

* **Brute Force:** Easy to understand, but inefficient when `D` is large.
* **Better:** Useful when extra memory is acceptable.
* **Optimal:** Best when we need `O(n)` time and `O(1)` extra space.

## Time & Space Summary

| Approach    |       Time |  Space |
| ----------- | ---------: | -----: |
| Brute Force | `O(n × D)` | `O(1)` |
| Better      |     `O(n)` | `O(D)` |
| Optimal     |     `O(n)` | `O(1)` |

## Lesson Learned

* Rotation is a reusable array pattern.
* The first `D` elements can be treated as one group.
* The reversal algorithm rotates the array without using an extra array.
* Complexity should be derived by counting the actual work performed.
* `D % n` avoids unnecessary full rotations.

## Next Topic

Right Rotate an Array by D Positions


