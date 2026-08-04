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