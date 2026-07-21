# Left Rotate an Array by One Position

## Problem Statement

Given an array, rotate all elements to the **left by one position**. The first element should move to the last position while all other elements shift one position to the left.

---

## Example

**Input**

```text
[2, 3, 4, 5, 6]
```

**Output**

```text
[3, 4, 5, 6, 2]
```

---

## Intuition

During a left rotation, the first element would be overwritten when shifting the remaining elements. To avoid losing it, store the first element in a temporary variable. Then shift every next element one position to the left and finally place the saved element at the last position.

---

## Brute Force Approach

* Perform one left rotation at a time.
* If multiple rotations are required, repeat the one-position rotation for each rotation.

**Time Complexity:** `O(n × k)` (for rotating by `k` positions)

**Space Complexity:** `O(1)`

---

## Better Approach

* Store the first **k** elements in a temporary array.
* Shift the remaining elements to the left by `k` positions.
* Copy the saved elements to the last `k` positions.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(k)`

---

## Optimal Approach (Today's Solution)

* Store the first element in a temporary variable.
* Traverse the array from the first index to the second-last index.
* Move the next element into the current position.
* Place the saved element in the last position.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

---

## Time Complexity

* The loop traverses the array once.
* If the array has `n` elements, the loop runs `n - 1` times.
* In Big-O notation, `n - 1` is simplified to `O(n)` because constants and lower-order terms are ignored for large inputs.

**Final Time Complexity:** `O(n)`

---

## Space Complexity

Only one extra variable (`temp`) is used regardless of the array size.

**Final Space Complexity:** `O(1)`

---

## Real World Applications

* Music playlist rotation
* Round Robin CPU Scheduling
* Circular Queue implementation
* Ring Buffer
* Game turn rotation
* Network load balancing

---

## Lesson Learned

* Rotation means changing positions while preserving every element.
* Save data before it gets overwritten.
* Think about the direction of movement before writing code.
* Build the algorithm first, then write pseudocode, and finally implement it.
* Time and Space Complexity should be derived by counting operations and extra memory, not memorized.

---

## Next Topic

Left Rotate an Array by **K** Positions
