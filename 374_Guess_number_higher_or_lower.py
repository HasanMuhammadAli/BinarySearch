class Solution:
    def __init__(self, pick):
        # Assume the correct number to guess
        self.pick = pick

    def guess(self, num: int) -> int:
        if num == self.pick:
            return 0
        elif num < self.pick:
            return 1
        else:
            return -1

    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = self.guess(mid)  # Calls the local guess function

            if result == 0:
                return mid
            elif result > 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# Example usage:
pick = 6  # Let's say the target number is 6
solution = Solution(pick)
n = 10  # The range is from 1 to 10
print(solution.guessNumber(n))  # Output should be 6
