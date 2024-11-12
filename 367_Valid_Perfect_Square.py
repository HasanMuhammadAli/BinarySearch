def isPerfectSquare(num):
    # Base case: if num is 1, return True because 1 is a perfect square
    if num == 1:
        return True

    # Initialize pointers
    low, high = 2, num // 2

    # Binary search
    while low <= high:
        mid = (low + high) // 2
        squared = mid * mid

        # Check if we found the perfect square
        if squared == num:
            return True
        elif squared > num:
            high = mid - 1
        else:
            low = mid + 1

    # If loop exits without finding a perfect square, return False
    return False
