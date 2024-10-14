def count_down(n):
    """
    Function to return a list of integers from n to 1 using recursion.
    
    Parameters:
    n (int): The positive integer representing the starting point of the range.
    
    Returns:
    list: A list of integers from n to 1.
    """
    # Your code here
    if n<=0:
        return 
    print(n)
    count_down(n-1)
    

    # Your code here
    if n == 1:
        return [1]
    return [n]+count_down(n-1)

print(count_down(5))