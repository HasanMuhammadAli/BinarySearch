def firstBadVersion(n):
    lo = 1  # Versions are usually 1-based
    hi = n
    ans = 0
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if isBadVersion(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return ans

# Example function to simulate the isBadVersion API
def isBadVersion(version):
    # Let's assume version 4 and onward are bad versions
    return version >= 4

# Example to demonstrate the function
n = 10  # Suppose there are 10 versions
print("The first bad version is:", firstBadVersion(n))