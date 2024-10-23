def permutations(s):
    """
    Function to generate all permutations of a string using recursion.
    
    Parameters:
    s (str): The string to generate permutations from.
    
    Returns:
    list of str: A list containing all permutations of the string.
    """
    # Your code here
    if(s==''):
        return ['']
        
    currentChar = s[0] 
    permutationString = permutations(s[1:])
    
    
    ans = []
    
    for eachPerm in permutationString:
        
        for position in range(0,len(eachPerm)+1):
            ans.append(eachPerm[0:position]+currentChar+eachPerm[position:])
            
    return ans        
