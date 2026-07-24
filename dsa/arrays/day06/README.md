# Remove Duplicates from Sorted Array

## Problem

Given a sorted array, remove duplicate elements in-place so that each unique element appears only once. Return the number of unique elements.

---

## Pattern

**Two Pointers**

---

## Key Idea

Since the array is already sorted, duplicate elements are always adjacent.

- Use a **Read Pointer** to scan the array.
- Use a **Write Pointer** to store only unique elements.
- Whenever the current element is different from the previous one:
  - Move the Write Pointer.
  - Copy the current element to the Write Pointer position.

---

## Algorithm

1. If the array has only one element, return `1`.
2. Initialize `write = 0`.
3. Traverse the array from index `1`.
4. If the current element is different from the previous element:
   - Increment `write`.
   - Copy the current element to `nums[write]`.
5. Return `write + 1`.

---

## Example

Input

```text
[1,1,2,2,3]
```

Output

```text
Unique Count = 3

Modified Array:
[1,2,3,_,_]
```

---

## Time Complexity

**O(n)**

- The array is traversed only once.

---

## Space Complexity

**O(1)**

- Only one extra pointer (`write`) is used.

---

## Concepts Learned

- Arrays
- Two Pointers
- In-place Modification
- Linear Traversal
- Time Complexity Analysis