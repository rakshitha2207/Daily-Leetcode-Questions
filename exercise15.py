def linear_search(arr, target):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    # Your code here
    return helper_linear_search(arr,target,index=0)
    
    
def helper_linear_search(arr,target,index):
    
    if(len(arr)==index):
         return False
     
     
    if(arr[index]==target):
         return True
    
    
    return helper_linear_search(arr,target,index+1)
         
         
