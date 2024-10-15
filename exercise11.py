def find_indicesHelper(arr, element,index):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code here
    if(len(arr)==index):
        return
    
    if(arr[index]==element):
        print(index)
    
    find_indicesHelper(arr,element,index+1)


    

def find_indices(arr,element):
    find_indicesHelper(arr,element,index=0)


find_indices([1,2,3,2,4,5,2],10)


def find_indices(arr, element):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code here
    def helper(index):
        if index == len(arr):
            return []
            
           
        if arr[index] == element:
            return [index] + helper(index + 1)
        else:
            return helper(index + 1)
        
        
    return helper(0)