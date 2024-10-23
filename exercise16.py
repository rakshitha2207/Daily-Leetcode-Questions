def Merge(arr, s, m, e):

    i = s
    j = m + 1
    ans = []

    while i <= m and j <= e:
        if arr[i] < arr[j]:
            ans.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            ans.append(arr[j])
            j += 1
        elif arr[i] == arr[j]:
            ans.append(arr[i])
            ans.append(arr[j])
            i += 1
            j += 1

    while i <= m:
        ans.append(arr[i])
        i += 1

    while j <= e:
        ans.append(arr[j])
        j += 1

    startOfMyAns = 0
    startOfMyList = s

    while startOfMyList <= e:
        arr[startOfMyList] = ans[startOfMyAns]
        startOfMyAns += 1
        startOfMyList += 1



def MergeSortHelper(arr, s, e):
    if s >= e:
        return

    m = s + (e - s) // 2

    MergeSortHelper(arr, s, m)
    MergeSortHelper(arr, m + 1, e)

    Merge(arr, s, m, e)



def merge_sort(arr):
    MergeSortHelper(arr, 0, len(arr)-1)
    return arr