# https://leetcode.com/problems/maximum-subarray/
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = -math.inf
        curr_sub_array = max_sub_array
        for n in nums:
            curr_sub_array = max(curr_sub_array, 0)
            curr_sub_array += n
            max_sub_array = max(max_sub_array, curr_sub_array)
        return max_sub_array


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Output: 6
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    # Input: nums = [1]
    # Output: 1
    print(solution.maxSubArray([1]))

    # Input: nums = [-1]
    # Output: -1
    print(solution.maxSubArray([-1]))

    # Input: nums = [5, 4, -1, 7, 8]
    # Output: 23
    print(solution.maxSubArray([5, 4, -1, 7, 8]))
