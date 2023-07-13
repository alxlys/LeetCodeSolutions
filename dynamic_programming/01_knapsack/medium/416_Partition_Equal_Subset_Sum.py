# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List


class Solution:
    # correct but slow solution
    # def canPartition(self, nums: List[int]) -> bool:
    #     total_sum = sum(nums)
    #     if total_sum % 2:
    #         return False
    #     target = total_sum // 2
    #
    #     def dfs(i, curr_sum):
    #         if curr_sum == target:
    #             return True
    #         if curr_sum > target or i == len(nums):
    #             return False
    #
    #         if dfs(i + 1, curr_sum):
    #             return True
    #
    #         return dfs(i + 1, curr_sum + nums[i])
    #
    #     return dfs(0, 0)

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            next_dp = set()
            for t in dp:
                include = t + nums[i]
                if include == target:
                    return True
                next_dp.add(t)
                next_dp.add(include)
            dp = next_dp
        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 5, 11, 5]
    # Output: true
    print(solution.canPartition([1, 5, 11, 5]))

    # Input: nums = [1, 2, 3, 5]
    # Output: false
    print(solution.canPartition([1, 2, 3, 5]))
