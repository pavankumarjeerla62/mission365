# Problem: Find the Largest Element in an Array
arr = [3, 5, 7, 2, 8, 1]

def largest_element(arr):

# Assume the first element is the largest.
# It becomes our starting point for comparison.
    largest = arr[0]

    # Visit every element in the array one by one.
    for num in arr:

        # Update the largest element if a bigger value is found.
        if num > largest:
            largest = num

    # Return the largest element found after scanning the array.
    return largest

print("The largest element in the array is:", largest_element(arr))


'''or
'''
# this is the way to take input from user of perfect size of array and also check if the input is valid or not
# n = int(input("Enter number of elements: "))
# this will convert the input string into a list of integers
# arr = list(map(int, input("Enter the elements: ").split()))

# this is to check if the number of elements entered is equal to the size of the array specified by the user
# if len(arr) != n:
#     print("Error: Number of elements does not match the given size.")
# else:
#     print("Valid input!")

# this is the way to take input but by defalt it will take the input as string 
# and convert it into list of integers
# arr = list(map(int, input().split()))

# # this neat step by step process like above 

# # Step 1: Read one line of text
# data = input()

# # Step 2: Break the text into individual values
# words = data.split()

# # Step 3: Convert every value from string to integer
# numbers = map(int, words)

# # Step 4: Store the converted values in a list
# arr = list(numbers)