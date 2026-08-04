arr = [4,0,5,0,0,8]

def move_zeros(arr):
    
    write = 0
    
    for read in range(len(arr)):

        if arr[read] != 0:

            arr[write] = arr[read]

            write += 1

    while write < len(arr):

        arr[write] = 0

        write += 1

move = move_zeros(arr)
print(arr)