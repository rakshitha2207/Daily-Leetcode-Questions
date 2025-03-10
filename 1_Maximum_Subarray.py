# Kadane's algorithm to find maximum sub array
def max_subarray(arr, max_sum):
    cur_sum = 0
    n = len(arr)
    for i in range(n):
        cur_sum += arr[i]
        max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum


arr = [-2, 4, 3,-5]
max_sum = arr[0]
print(max_subarray(arr, max_sum))



# Printing all the sub arrays
def print_subarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # Print subarray from i to j
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()
    print("\n")            


arr = [-2, 4, 3, -5]
print_subarray(arr)


