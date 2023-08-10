# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k - 1
        nums.sort()
        res = math.inf
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [90], k = 1
    # Output: 0
    print(solution.minimumDifference([90], 1))

    # Input: nums = [9, 4, 1, 7], k = 2
    # Output: 2
    print(solution.minimumDifference([9, 4, 1, 7], 2))
