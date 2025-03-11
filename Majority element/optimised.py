import math

def majority_element(arr):
    arr = sorted(arr)
    freq = 1
    ans = arr[0]
    for ele in arr:
        if ele==ans:
            freq += 1
        else:
            ans = ele
            freq = 1    
        if(freq > math.floor(len(arr)/2)):
           return ans  
    return -1      


arr = [1,2,3,4]
ans = majority_element(arr)
print(ans)