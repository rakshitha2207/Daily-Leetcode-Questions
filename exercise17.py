def quick_sort(arr):
    QuickSort(arr,0,len(arr)-1)
    return arr


def PartitionFunction(arr,s,e):
    pivot = arr[e]
    i = s
    rightPosition = s

    while(i<=e-1):
        if(arr[i]<pivot):
            rightPosition+=1
        i+=1
    arr[rightPosition], arr[e] = arr[e], arr[rightPosition]

    pivotIndex = rightPosition

    start = s
    end = e

    while(start<pivotIndex and end>pivotIndex):
        if(arr[start]<pivot):
            start+=1  
        elif(arr[end]>=pivot):
            end-=1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1

    return pivotIndex                      


def QuickSort(arr,s,e):
    if s>=e:
        return
    
    pivotIndex = PartitionFunction(arr,s,e)

    QuickSort(arr,s,pivotIndex-1)
    QuickSort(arr,pivotIndex+1,e)


arr=[3,6,7,2,1,4,5,4]
quick_sort(arr)
print(arr)