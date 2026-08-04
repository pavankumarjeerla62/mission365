arr = [4,0,5,0,0,8]

def move_zeros(arr):

    # Write pointer starts from the first index
    write = 0

    # Read every element in the array
    for read in range(len(arr)):

        # Process only non-zero elements
        if arr[read] != 0:

            # Copy the non-zero element to the write position
            arr[write] = arr[read]

            # Move the write pointer to the next position
            write += 1

    # Fill the remaining positions with zeroes
    while write < len(arr):

        arr[write] = 0

        # Move the write pointer forward
        write += 1

# Call the function to modify the array
move = move_zeros(arr)

# Print the updated array
print(arr)