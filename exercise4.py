def count_digits(n):
    """
    Function to find the number of digits in a number using recursion.
    
    Parameters:
    n (int): The positive integer whose digits are to be counted.
    
    Returns:
    int: The number of digits in the integer.
    """
    # Your code here
    if n>=1 and n<=9:
        return 1
    if n==0:
        return 1
    return 1 + count_digits(n//10)


print(count_digits(0))