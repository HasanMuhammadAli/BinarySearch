def searchInsert(arr,x):
    n = len(arr)  # size of the array
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans


arr = [1, 2, 4, 7]
x = 6
ind = searchInsert(arr, x)
print("The index is:", ind)