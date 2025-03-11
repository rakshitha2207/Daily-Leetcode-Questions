def pairsum(arr, target_sum): #O(n2)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pair_sum = arr[i] + arr[j]
            if(pair_sum == target_sum):
                return [i,j]
            
    return None        


arr = [2,4,6,7]
target_sum =11
ans = pairsum(arr,target_sum)
print(ans)