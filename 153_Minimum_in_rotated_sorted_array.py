def minimumInRotatedArray(arr):
    low = 0
    high = len(arr)-1
    ans=max(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            ans=min(arr[low],ans)
            low=mid+1
        else:
            ans=min(arr[mid],ans)
            high=mid-1
    return ans

arr=[7,8,1,2,3,4,5,6]
ans=minimumInRotatedArray(arr)
print(ans)