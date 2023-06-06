# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0, 0
        for n in nums:
            temp = max(rob_1 + n, rob_2)
            rob_1 = rob_2
            rob_2 = temp
        return rob_2


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3, 1]
    # Output: 4
    print(solution.rob([1, 2, 3, 1]))

    # Input: nums = [2, 7, 9, 3, 1]
    # Output: 12
    print(solution.rob([2, 7, 9, 3, 1]))
