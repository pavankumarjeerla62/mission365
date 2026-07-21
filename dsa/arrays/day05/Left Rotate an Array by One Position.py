# Left Rotate an Array by One Position

arr = [1, 2, 3, 4, 5, 6]

def leftRotate(arr):
    # Save the first element before shifting
    temp = arr[0]

    # Shift all elements one position to the left
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    # Place the saved element at the last position
    arr[len(arr) - 1] = temp

    return arr

print(leftRotate(arr))


# --------------------------------------------
# Better Idea: Left Rotate an Array by 3 Positions
# --------------------------------------------
arr = [10, 20, 30, 40, 50, 60]

def leftRotate(arr):
    # Save the first 3 elements
    temp = arr[0:3]

    # Shift remaining elements 3 positions to the left
    for i in range(len(arr) - 3):
        arr[i] = arr[i + 3]

    # Place the saved elements at the end
    arr[len(arr) - 3 : len(arr)] = temp

    return arr

print(leftRotate(arr))



