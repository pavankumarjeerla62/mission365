#duplicate in sorted array

nums=[0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    # If there is only one element, it is already unique
    if len(nums) == 1:
        return 1

    # Write pointer starts at the first unique element
    write = 0

    # Read the array from the second element
    for i in range(1, len(nums)):

        # If a new unique element is found
        if nums[i] != nums[i - 1]:

            # Move the write pointer to the next position
            write += 1

            # Place the unique element at the write pointer
            nums[write] = nums[i]

    # Return the number of unique elements
    return write + 1


unique_count = removeDuplicates(nums)
print("Array after removing duplicates:", nums[:unique_count])
print("Number of unique elements:", unique_count)