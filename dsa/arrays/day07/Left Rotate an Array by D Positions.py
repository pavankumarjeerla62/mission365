# Left Rotate an Array by D Positions

def reverse(arr, start, end):
    # Reverse the elements between start and end
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr, d):
    n = len(arr)

    # Handle an empty array
    if n == 0:
        return arr

    # Reduce unnecessary rotations
    d = d % n

    # Reverse the first D elements
    reverse(arr, 0, d - 1)

    # Reverse the remaining elements
    reverse(arr, d, n - 1)

    # Reverse the complete array
    reverse(arr, 0, n - 1)

    return arr


# Example
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3

print(left_rotate(arr, d))