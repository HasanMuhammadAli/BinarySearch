def minimumInRotatedArray(arr):
    low = 0
    high = len(arr)-1
    ans=max(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            if arr[low] < ans :
                index = low
                ans = arr[low]
            low=mid+1
        else:
            if arr[mid] < ans :
                index = mid
                ans = arr[mid]
            high=mid-1
    return index,ans

arr=[5,1,2,3,4]
index,ans=minimumInRotatedArray(arr)
print(f"Number of times array has been rotated is {index}")
print(f"Minimum value in rotated Array is {ans}")