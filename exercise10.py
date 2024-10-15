# Finding the last index of a given element
def find_last_index(arr,element):
    if len(arr)==0:
        return -1
    if arr[len(arr)-1]==element:
        return len(arr)-1
    
    ans = find_last_index(arr[:-1],element)
    return ans


print(find_last_index([1,2,3,4,5,2,4],10))


