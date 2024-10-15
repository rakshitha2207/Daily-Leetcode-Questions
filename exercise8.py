def recursive_sum(arr):
    """
    Function to calculate the sum of an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    
    Returns:
    int: The sum of the array elements.
    """
    # Your code here
    if(len(arr)==0):
        return 0
    sumofleftoverarray = recursive_sum(arr[1:])
    ans = sumofleftoverarray + arr[0]
    return ans


def recursive_sum_tail(arr,acc=0):
    if(len(arr)==0):
        return acc
    acc += arr[0]
    return recursive_sum_tail(arr[1:],acc)

print(recursive_sum_tail([1,2,3,4]))
    