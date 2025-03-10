def chocolate_factory(arr):
    L = [0 for j in range(len(arr))]
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            L[j] = arr[i]
            j += 1
    return L      


arr = [4,0,5,0,6,4,0,8,0,1]
print(chocolate_factory(arr))