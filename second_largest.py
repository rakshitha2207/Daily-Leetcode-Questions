# def second_largest(arr):
#     arr = sorted(arr)
#     return arr[-2]        




def second_largest(arr):
    max1 = 0
    max2 = 0
    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
    return max1, max2        


arr = [1, 7, 10, 3, 11]
ans = second_largest(arr)
print(ans)