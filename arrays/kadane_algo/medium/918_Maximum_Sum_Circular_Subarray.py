# https://leetcode.com/problems/maximum-sum-circular-subarray/
import math
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, curr_min, total = nums[0], nums[0], nums[0]
        glob_max, glob_min = curr_max, curr_min
        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            curr_min = min(curr_min + nums[i], nums[i])
            glob_max = max(curr_max, glob_max)
            glob_min = min(curr_min, glob_min)
            total += nums[i]
        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, -2, 3, -2]
    # Output: 3
    print(solution.maxSubarraySumCircular([1, -2, 3, -2]))

    # Input: nums = [5, -3, 5]
    # Output: 10
    print(solution.maxSubarraySumCircular([5, -3, 5]))

    # Input: nums = [-3, -2, -3]
    # Output: -2
    print(solution.maxSubarraySumCircular([-3, -2, -3]))
