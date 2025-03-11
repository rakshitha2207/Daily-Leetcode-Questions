def pairsum(arr, target_sum): #O(n)
    i = 0
    j = len(arr)-1

    while i < j:
        pair_sum = arr[i] + arr[j]
        if(pair_sum < target_sum):
            i += 1
        elif (pair_sum > target_sum):
            j -= 1
        else:
          return [i, j]
        
    return ("No match found")    
    
arr = [2,4,6,7]
target_sum = 100
ans = pairsum(arr,target_sum)
print(ans)