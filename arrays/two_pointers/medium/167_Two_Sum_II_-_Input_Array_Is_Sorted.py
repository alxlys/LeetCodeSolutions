# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


if __name__ == '__main__':
    solution = Solution()

    # Input: numbers = [2, 7, 11, 15], target = 9
    # Output: [1, 2]
    print(solution.twoSum([2, 7, 11, 15], 9))

    # Input: numbers = [2, 3, 4], target = 6
    # Output: [1, 3]
    print(solution.twoSum([2, 3, 4], 6))

    # Input: numbers = [-1, 0], target = -1
    # Output: [1, 2]
    print(solution.twoSum([-1, 0], -1))
