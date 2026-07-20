# Problem: Check if an Array is Sorted

# Example array
arr = [3,4,5,1,2]

def check_sorted(arr):

    # Traverse the array until the second last element.
    # We stop at len(arr) - 1 because we compare arr[i] with arr[i + 1].
    for i in range(len(arr) - 1):

        # If the current element is greater than the next element,
        # the ascending order is broken.
        if arr[i] > arr[i + 1]:
            
            return False
            

    # If no pair breaks the order,
    # the entire array is sorted.
    return True

# Print the result returned by the function.
print(check_sorted(arr))


