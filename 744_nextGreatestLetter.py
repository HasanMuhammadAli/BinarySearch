def nextGreatestLetter(letters, target):
    # If the first letter in the list is greater than the target, return it
    if letters[0] > target:
        return letters[0]

    # Initialize pointers and answer variable
    left, right = 0, len(letters) - 1
    answer = -1

    # Binary search
    while left <= right:
        mid = (left + right) // 2

        # Check if letters[mid] is greater than target
        if letters[mid] > target:
            answer = letters[mid]  # Store the potential answer
            right = mid - 1       # Move the right pointer to search for a smaller letter
        else:
            left = mid + 1        # Move the left pointer to search for a larger letter

    # Return the answer; if not found, wrap around to the first element
    return answer if answer != -1 else letters[0]
