import math # O(n^2)

def majority_element(arr):
    for value in arr:
        count = 0
        for ele in arr:
            if(ele==value):
                count +=1
        if(count > math.floor(len(arr)/2)):
            return value
    return None             



arr = [1,2,3,4]
ans = majority_element(arr)
print(ans)