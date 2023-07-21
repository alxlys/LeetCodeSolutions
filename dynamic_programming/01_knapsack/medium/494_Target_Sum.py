# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    # correct but slow solution
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     length = len(nums)
    #     count_path = []
    #
    #     def dfs(i, total):
    #         if i == length:
    #             if total == target:
    #                 count_path.append(1)
    #             return
    #         dfs(i + 1, total + nums[i])
    #         dfs(i + 1, total - nums[i])
    #
    #     dfs(0, 0)
    #     return len(count_path)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 1, 1, 1, 1], target = 3
    # Output: 5
    print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))

    # Input: nums = [1], target = 1
    # Output: 1
    print(solution.findTargetSumWays([1], 1))
