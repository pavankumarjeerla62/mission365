# Check if an Array is Sorted

## Problem Statement

Given an array, determine whether it is sorted in ascending order.

Example:

Input:

```
[1, 2, 3, 4, 5]
```

Output:

```
True
```

---

## Intuition

Instead of comparing every element with all other elements, we only need to compare each element with its next adjacent element. If we find even one pair where the current element is greater than the next element, the array is not sorted.

---

## Brute Force Approach

* Compare every element with every other element.
* This approach performs unnecessary comparisons and is inefficient.

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(1)`

---

## Optimal Approach

* Traverse the array once.
* Compare `arr[i]` with `arr[i + 1]`.
* If `arr[i] > arr[i + 1]`, return `False`.
* If the loop finishes without finding any violation, return `True`.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

---

## Dry Run

Array:

```
[1, 2, 4, 5, 7, 6, 8]
```

Comparisons:

```
1 < 2 ✅
2 < 4 ✅
4 < 5 ✅
5 < 7 ✅
7 > 6 ❌
```

Result:

```
False
```

---

## Real World Applications

* Binary Search
* Merge Sort
* Two Pointer Technique
* Remove Duplicates from Sorted Array
* Data Validation before processing

---

## Key Takeaways

* Compare only adjacent elements.
* Stop immediately when the order is broken (Early Exit).
* A sorted array with `n` elements requires only `n - 1` comparisons.
* No extra space is required.

---

## Next Topic

Remove Duplicates from Sorted Array
