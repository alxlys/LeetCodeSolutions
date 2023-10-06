# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [2, 3, 1, 1, 4]
    # Output: true
    print(solution.canJump([2, 3, 1, 1, 4]))

    # Input: nums = [3, 2, 1, 0, 4]
    # Output: false
    print(solution.canJump([3, 2, 1, 0, 4]))
