# Problem: Find the Largest Element in an Array
arr = [3, 5, 7, 2, 8, 1]

def largest_element(arr):

    # Start by assuming the first element is the largest.
    # This gives us a valid starting point for comparison.
    largest = arr[0]

    # Visit every element in the array one by one.
    for num in arr:

        # If we find an element larger than our current answer,
        # update the answer.
        if num > largest:
            largest = num

    # Return the largest element found after scanning the array.
    return largest

print("The largest element in the array is:", largest_element(arr))


'''or
'''
# n = int(input("Enter number of elements: "))

# arr = list(map(int, input("Enter the elements: ").split()))

# if len(arr) != n:
#     print("Error: Number of elements does not match the given size.")
# else:
#     print("Valid input!")