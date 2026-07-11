# Problem: Find Second Largest Element in an Array 

# Brute Force Approach: Sort the array and find the second largest element.

arr = [8, 3, 15, 6, 11]

# Sort the array in ascending order.
arr.sort()

# The last element is the largest.
largest = arr[-1]

# Traverse from the second last element towards the beginning.
for i in range(len(arr) - 2, -1, -1):

    # The first element different from the largest
    # is the second largest.
    if arr[i] != largest:
        print("Second Largest:", arr[i])
        break

# Sorting = O(n log n)

# Traversal = O(n)

# Overall = O(n log n)



# Better Approach: Traverse the array once and find the second largest element.

# Problem: Second Largest Element in an Array (Better)

arr = [8, 3, 15, 6, 11]

# Step 1: Assume the first element is the largest.
largest = arr[0]

# Step 2: Find the largest element.
for num in arr:

    if num > largest:
        largest = num

# Step 3: Assume there is no second largest yet.
second_largest = -1

# Step 4: Traverse again.
for num in arr:

    # Ignore the largest element.
    # Update second largest whenever a bigger candidate is found.
    if num != largest and num > second_largest:
        second_largest = num

print("Second Largest:", second_largest)

# First Traversal = O(n)

# Second Traversal = O(n)

# Overall = O(n)





# Optimal Approach: Maintain both largest and second_largest.
# Update both in a single traversal.

# Problem: Second Largest Element in an Array (Optimal)

arr = [8, 3, 15, 6, 11]

# Step 1: Assume the first element is the largest.
largest = arr[0]

# Step 2: No second largest has been found yet.
second_largest = -1

# Step 3: Traverse the array.
for num in arr:

    # If current element becomes the new largest,
    # move the old largest to second largest.
    if num > largest:
        second_largest = largest
        largest = num

    # Otherwise, update second largest if the current element
    # is between largest and second largest.
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)

# Single Traversal = O(n)

# Overall = O(n)