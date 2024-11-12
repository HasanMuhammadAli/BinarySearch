def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # If target is found
        if nums[mid] == target:
            return mid

        # Check if the left part is sorted
        if nums[left] <= nums[mid]:
            # Check if the target is in the sorted left part
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Eliminate right half
            else:
                left = mid + 1   # Eliminate left half

        # Otherwise, the right part is sorted
        else:
            # Check if the target is in the sorted right part
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Eliminate left half
            else:
                right = mid - 1  # Eliminate right half

    # If target is not found
    return -1
