def firstOccurrence(arr, k):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            first = mid
            high = mid - 1  # continue searching to the left
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return first


def lastOccurrence(arr, k):
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            last = mid
            low = mid + 1  # continue searching to the right
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1

    return last


def searchRange(arr, k):
    first = firstOccurrence(arr, k)
    if first == -1:
        return [-1, -1]
    last = lastOccurrence(arr, k)
    return [first, last]
