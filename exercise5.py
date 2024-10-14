def fibonacci(n):
    """
    Function to calculate the nth Fibonacci number using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the Fibonacci number is to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Your code here
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)