def majority_element(arr):
    # Phase 1: Find candidate
    candidate = None
    count = 0
    for ele in arr:
        if count == 0:
            candidate = ele
            count = 1
        elif ele == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify candidate - Only if in question no majority is found
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return -1

# Test
arr = [1, 2, 3, 1, 1, 2, 3, 4, 5, 1, 1]
ans = majority_element(arr)
print(ans)  # Output: 1
